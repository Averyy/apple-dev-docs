# CMVideoCardGammaType

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Specifies a video card gamma profile tag.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMVideoCardGammaType {
    ...
} CMVideoCardGammaType;
```

## Topics

### Instance Properties
- [gamma](./cmvideocardgammatype/api-1560391-gamma.md)
  A structure that specifies the video card gamma data for the profile tag, as described in [`CMVideoCardGamma`](./cmvideocardgamma.md). 
- [reserved](./cmvideocardgammatype/api-1560260-reserved.md)
  This field is reserved and must contain the value 0.
- [typeDescriptor](./cmvideocardgammatype/api-1560647-typedescriptor.md)
  The signature type for a video card gamma tag. There is currently only one type possible, `cmSigVideoCardGammaType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatype)*