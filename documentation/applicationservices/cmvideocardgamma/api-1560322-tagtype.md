# tagType

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

A [Video Card Gamma Storage Types](../api-1560344-video_card_gamma_storage_types.md) constant that specifies the format of the data currently stored in the union. To determine the type of structure present in a specific instance of the `CMVideoCardGamma` structure, you test this union tag. If you are setting up a `CMVideoCardGamma` structure to store video card gamma data, you set `tagType` to a constant value that identifies the structure type you are using. The possible constant values are described in [Video Card Gamma Storage Types](../api-1560344-video_card_gamma_storage_types.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
UInt32 tagType;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmvideocardgamma/1560322-tagtype)*