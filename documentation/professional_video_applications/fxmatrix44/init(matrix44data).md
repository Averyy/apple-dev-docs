# init(matrix44Data:)

**Framework**: Professional Video Applications  
**Kind**: init  
**Role**: Initializer

Initializes a matrix with the specified data.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
init!(matrix44Data newMatrix: UnsafeMutablePointer<(Double, Double, Double, Double)>!)
```

```objc
- (id) initWithMatrix44Data:(Matrix44Data) newMatrix;
```

## Return Value

An initialized matrix object or `nil` if the object couldn’t be created.

## Parameters

- `newMatrix`: The new matrix data.

## See Also

### Creating and Initializing a Matrix
- [init!()](./init%28%29.md)
  Initializes the matrix to the identity matrix.
- [init!(fxMatrix: FxMatrix44!)](./init%28fxmatrix%29.md)
  Initializes the matrix using the specified matrix object.
- [init!(colorMatrix44Data: UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./init%28colormatrix44data%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxmatrix44/init(matrix44data:))*