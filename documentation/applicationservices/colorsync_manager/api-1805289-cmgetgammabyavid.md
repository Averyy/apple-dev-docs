# CMGetGammaByAVID

**Framework**: Application Services  
**Kind**: func

Obtains the gamma value for the specified display device.

## Declaration

```c
CMError CMGetGammaByAVID (
   CMDisplayIDType theID,
   CMVideoCardGamma *gamma,
   UInt32 *size
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `theID`: A Display Manager ID value. You pass the ID value for the display device for which to set the gamma.
- `gamma`: 
- `size`: 

## See Also

### Working With Video Card Lookup Tables
- [CMSetGammaByAVID](./api-1805291-cmsetgammabyavid.md)
  Sets the gamma for the specified display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805289-cmgetgammabyavid)*