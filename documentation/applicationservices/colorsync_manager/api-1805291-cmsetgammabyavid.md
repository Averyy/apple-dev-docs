# CMSetGammaByAVID

**Framework**: Application Services  
**Kind**: func

Sets the gamma for the specified display device.

## Declaration

```c
CMError CMSetGammaByAVID (
   CMDisplayIDType theID,
   CMVideoCardGamma *gamma
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Parameters

- `theID`: A Display Manager ID value. You pass the ID value for the display device for which to set the gamma.
- `gamma`: A pointer to the gamma value to which you want to set the display device. 

## See Also

### Working With Video Card Lookup Tables
- [CMGetGammaByAVID](./api-1805289-cmgetgammabyavid.md)
  Obtains the gamma value for the specified display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805291-cmsetgammabyavid)*