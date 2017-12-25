# pymp4decrypt
A Python MP4 decrypter for CENC encrypted MP4s

`pymp4decrypt` uses the excellent parsing library by [beardypig](https://github.com/beardypig), but with some extra [modifications](https://github.com/truedread/pymp4) for CENC boxes.

# Usage

By itself as a script:

```python decrypt.py -k KEY -i INPUT_FILE_ENCRYPTED.mp4 -o OUTPUT_FILE_DECRYPTED.mp4```

As a library:

```python
>>> import binascii
>>> import pymp4decrypt
>>> enc = open('encrypted.mp4', 'rb')
>>> dec = open('decrypted.mp4', 'wb')
>>> key = binascii.unhexlify('4ce68c303ae037a59888d4866de39ffb')
>>> pymp4decrypt.decrypt(key, enc, dec)
>>> 
```