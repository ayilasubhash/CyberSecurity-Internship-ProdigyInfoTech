from PIL import Image
import numpy as np
import argparse
import random

def process_image(image_path, method='add', key=50, swap_block_size=32):
    """Core function to handle both encryption and decryption"""
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: File '{image_path}' not found")
        return None
        
    pixels = np.array(img)
    
    if method == 'add':
        processed = (pixels + key) % 256 if key >= 0 else (pixels - abs(key)) % 256
    elif method == 'xor':
        processed = np.bitwise_xor(pixels, key)
    elif method == 'swap':
        processed = pixel_swapping(pixels, swap_block_size, key)
    else:
        raise ValueError("Invalid method. Choose 'add', 'xor', or 'swap'")
    
    return Image.fromarray(processed.astype('uint8'))

def pixel_swapping(arr, block_size, seed):
    """Swap pixel blocks using a random seed for encryption/decryption"""
    random.seed(seed)
    h, w = arr.shape[:2]
    
    # Create block grid
    blocks = []
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            blocks.append(arr[y:y+block_size, x:x+block_size])
    
    # Shuffle blocks using seed
    random.shuffle(blocks)
    
    # Reassemble image
    swapped = np.zeros_like(arr)
    idx = 0
    for y in range(0, h, block_size):
        for x in range(0, w, block_size):
            swapped[y:y+block_size, x:x+block_size] = blocks[idx]
            idx += 1
    return swapped

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Encryption Tool')
    parser.add_argument('input', help='Input image path')
    parser.add_argument('output', help='Output image path')
    parser.add_argument('-m', '--method', choices=['add', 'xor', 'swap'], 
                        default='add', help='Encryption method')
    parser.add_argument('-k', '--key', type=int, default=50,
                        help='Encryption key (integer)')
    parser.add_argument('-d', '--decrypt', action='store_true',
                        help='Decrypt mode (use negative key for additive method)')

    args = parser.parse_args()
    
    if args.method in ['add', 'xor'] and args.decrypt:
        args.key = -args.key if args.method == 'add' else args.key
    
    result = process_image(
        args.input,
        method=args.method,
        key=args.key,
        swap_block_size=32
    )
    
    if result:
        result.save(args.output)
        print(f"Operation completed successfully. Saved to {args.output}")
