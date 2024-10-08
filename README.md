# VidEmbed: Video Data Embedding Algorithm

This project implements algorithms for converting files into binary format and embedding data into video frames using pixel manipulation techniques. It focuses on preserving video quality while securely hiding information, making it robust against common video compression methods like those used by YouTube.

## Key Features:
1. **File Conversion**:
   - Convert any file to binary format and reconstruct the file from binary data.
2. **Data Embedding**:
   - Embed binary data within video frames by manipulating a 10x10 pixel block in each frame.
   - Currently, the algorithm adds 1 bit per frame, but it can be modified to store more bits per frame.
3. **Data Extraction**:
   - Extract embedded binary data from video frames by analyzing pixel values in the manipulated 10x10 block.
4. **Quality Preservation**:
   - Ensures minimal visual distortion even after compression, using averaging techniques for robustness.
5. **Tested on YouTube Compression**:
   - Tested on videos compressed by YouTube.

## Applications:
- **Digital Watermarking**: Embed ownership or copyright information in video content.
- **Secure Communication**: Hide sensitive information within video files for secure transfer.
- **Data Storage**: Store small amounts of data within videos without risk of it being easily extracted or stolen.


**Easy to use the scripts, just clone and get started after having the required packages installed.**


## Disclaimer: 
**This project is for educational purpose. I do not endorse or support any illicit use of the algorithm. Please use responsibly and ethically.**
