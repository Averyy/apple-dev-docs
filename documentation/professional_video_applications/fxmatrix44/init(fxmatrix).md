# init(fxMatrix:)

**Framework**: Professional Video Applications  
**Kind**: init  
**Role**: Initializer

Initializes the matrix using the specified matrix object.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
init!(fxMatrix newFxMatrix: FxMatrix44!)
```

```objc
- (id) initWithFxMatrix:(FxMatrix44 *) newFxMatrix;
```

## Return Value

An initialized matrix object or `nil` if the object couldn’t be created.

## Parameters

- `newFxMatrix`: A 4 x 4 matrix object.

## See Also

### Creating and Initializing a Matrix
- [init!()](./init%28%29.md)
  Initializes the matrix to the identity matrix.
- [init!(matrix44Data: UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./init%28matrix44data%29.md)
  Initializes a matrix with the specified data.
- [init!(colorMatrix44Data: UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./init%28colormatrix44data%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxmatrix44/init(fxmatrix:))*