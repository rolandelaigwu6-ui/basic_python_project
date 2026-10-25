
🛠️ Phase-by-Phase Instructions


Phase 1: Stream Parsing & File Validation

• Action: Securely ingest an image file using PIL.Image. Ensure your application reads the raw binary dimensions (Width × Height) and extracts the pixel stream.



Phase 2: Aspect Ratio & Downsampling Calculations

• Action: Compute the target width constraint while preserving the original image's aspect ratio. Apply a scaling coefficient (typically 0.5 to 0.55) to the height axis.


Phase 3: Dimensional Luminosity Normalization

• Action: Convert the 3-channel RGB pixel values into a single 8-bit scale channel (0 to 255).
• Mathematical Formula: Apply standard luminance weighting rather than a simple math average to match human visual perception:



Phase 4: Token Quantization & Mapping

• Action: Take the 0-255 brightness integer and slice it dynamically across a fixed array of text glyphs ordered by pixel density (e.g., ["@", "#", "W", "•", ".", " "]).
• Mapping Math:

0
Phase 5: Buffer Rendering & Output

• Action: Iterate through the parsed string array. Insert newline escape tokens (\n) exactly at every multi-column width interval to output a uniform 2D block to the shell or a .txt artifact file.