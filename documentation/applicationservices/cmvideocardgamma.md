# CMVideoCardGamma

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains video gamma data to store with a video gamma profile tag. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMVideoCardGamma {
    ...
} CMVideoCardGamma;
```

#### Overview

The ColorSync Manager defines the `CMVideoCardGamma` data structure to specify the video gamma data to store with a video gamma profile tag. The structure is a union that can store data in either table or formula format. 

## Topics

### Fields
- [table](./cmvideocardgamma/api-1806487-table.md)
  A structure of type `CMVideoCardGammaTable`. If the `tagType` field has the value `cmVideoCardGammaTableType`, the `CMVideoCardGamma` structure’s union field should be treated as a table, as described in [`CMVideoCardGammaTable`](./cmvideocardgammatable.md). 
- [formula](./cmvideocardgamma/api-1806493-formula.md)
### Instance Properties
- [tagType](./cmvideocardgamma/api-1560322-tagtype.md)
  A [Video Card Gamma Storage Types](./api-1560344-video_card_gamma_storage_types.md) constant that specifies the format of the data currently stored in the union. To determine the type of structure present in a specific instance of the `CMVideoCardGamma` structure, you test this union tag. If you are setting up a `CMVideoCardGamma` structure to store video card gamma data, you set `tagType` to a constant value that identifies the structure type you are using. The possible constant values are described in [Video Card Gamma Storage Types](./api-1560344-video_card_gamma_storage_types.md).
- [u](./cmvideocardgamma/api-1560238-u.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmvideocardgamma)*