# setMatrix(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Sets the matrix to the specified values.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func setMatrix(_ newMatrix: UnsafeMutablePointer<(Double, Double, Double, Double)>!)
```

```objc
- (void) setMatrix:(Matrix44Data) newMatrix;
```

## Parameters

- `newMatrix`: The new matrix values.

## See Also

### Getting and Setting the Matrix
- [func matrix() -> UnsafeMutablePointer<Matrix44Data>!](./matrix%28%29.md)
  Gets the raw matrix data.
- [func setToIdentity()](./settoidentity%28%29.md)
  Sets the matrix to the identity matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxmatrix44/setmatrix(_:))*