---
title: Data Representation and Encoding
level: foundation
---

Computers represent text, numbers, images, sound and video using binary data. Data representation defines how information is converted into forms that digital systems can store, process and transmit.

## 1. Binary Representation of Information

A computer fundamentally processes information using binary states represented by 0 and 1.

A bit is the smallest basic unit of digital information.

A group of eight bits is called a byte.

Binary representation is used for:

- Numerical values.
- Text characters.
- Images.
- Audio.
- Video.
- Program instructions.

## 2. Representation of Integers

Unsigned binary integers represent non-negative values.

For an n-bit unsigned number, the range is:

0 to 2^n - 1

For example, an 8-bit unsigned integer has a range of:

0 to 255.

Signed integers can represent both positive and negative values.

Two's complement is commonly used for signed integer representation.

For an n-bit two's complement number, the range is:

-2^(n-1) to 2^(n-1) - 1

For an 8-bit signed integer, the range is:

-128 to 127.

## 3. Representation of Real Numbers

Computers commonly represent real numbers using floating-point formats.

Floating-point representation contains:

- Sign.
- Exponent.
- Significand.

The IEEE 754 standard defines widely used floating-point formats.

Common formats include:

- Single precision: 32 bits.
- Double precision: 64 bits.

Floating-point representation can introduce rounding errors because many real numbers cannot be represented exactly using a finite number of binary digits.

## 4. Character Encoding

Character encoding assigns numerical values to characters so that computers can store and process text.

### ASCII

ASCII is a character encoding standard originally designed using seven bits.

It represents 128 characters, including:

- English letters.
- Decimal digits.
- Punctuation.
- Control characters.

Extended eight-bit systems may represent additional characters, but they are not all the same standard.

### Unicode

Unicode provides a universal system for assigning code points to characters from many writing systems.

It supports:

- English.
- Indian languages.
- Chinese.
- Arabic.
- Japanese.
- Mathematical symbols.
- Emoji.

### UTF-8

UTF-8 is a variable-length Unicode encoding.

It uses one to four bytes per Unicode code point.

UTF-8 is widely used on the internet.

## 5. Image Representation

Digital images consist of pixels.

A pixel is the smallest addressable picture element in a raster image.

Important image concepts include:

- Resolution: Number of pixels in an image.
- Colour depth: Number of bits used to represent pixel colour.
- RGB: Red, Green and Blue colour model.
- Compression: Reduction of image file size.

For a basic uncompressed image:

Image size = Width x Height x Bits per pixel

This calculation excludes additional file metadata and other storage overhead.

## 6. Audio Representation

Digital audio is created by sampling an analogue sound signal.

Important concepts include:

**Sampling rate:** Number of samples captured per second.

**Bit depth:** Number of bits used to represent each sample.

**Channels:** Number of separate audio channels, such as mono or stereo.

A simplified uncompressed audio bitrate calculation is:

Bitrate = Sampling rate x Bit depth x Number of channels

## 7. Data Compression

Compression reduces the amount of storage or transmission capacity required.

### Lossless Compression

Allows the original data to be reconstructed exactly.

Examples:
- ZIP.
- PNG.
- FLAC.

### Lossy Compression

Reduces file size by removing information that may be less noticeable or less important for the intended use.

Examples:
- JPEG.
- MP3.
- Many video compression formats.

## Common Exam Traps

- A bit is a binary digit.
- A byte contains eight bits.
- ASCII and Unicode are character encoding concepts.
- UTF-8 is a variable-length Unicode encoding.
- Pixels represent digital image elements.
- Sampling rate measures samples per second.
- Lossless compression preserves the original data exactly.
- Lossy compression does not guarantee exact reconstruction.

## Quiz

1. How many bits are used in one byte?

- [ ] 2.
- [ ] 4.
- [x] 8.
- [ ] 16.

> A byte consists of eight binary digits.

2. Which encoding is widely used to represent Unicode text on the internet?

- [ ] ASCII-7 only.
- [ ] Binary Coded Decimal.
- [x] UTF-8.
- [ ] Morse code.

> UTF-8 is a variable-length Unicode encoding widely used for web content and digital communication.

3. Which compression method allows exact reconstruction of the original data?

- [ ] Lossy compression.
- [ ] Perceptual compression.
- [ ] Irreversible compression.
- [x] Lossless compression.

> Lossless compression preserves all original information and allows exact reconstruction.