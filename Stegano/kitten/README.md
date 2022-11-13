# Solution for kitten

The technique used to hide secrets is called LSB steganography.

You can use a popular tool called __zsteg__ in order to recover the hidden flag.

![Using zsteg](data:image/png;base64,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)