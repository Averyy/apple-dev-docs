# matrix()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Gets the raw matrix data.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func matrix() -> UnsafeMutablePointer<Matrix44Data>!
```

```objc
- (Matrix44Data *) matrix;
```

#### Return Value

A pointer to a [`FxMatrix44`](../fxmatrix44.md).

## See Also

### Getting and Setting the Matrix
- [func setMatrix(UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./setmatrix%28_%29.md)
  Sets the matrix to the specified values.
- [func setToIdentity()](./settoidentity%28%29.md)
  Sets the matrix to the identity matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxmatrix44/matrix())*