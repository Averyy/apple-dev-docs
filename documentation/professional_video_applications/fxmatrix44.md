# FxMatrix44

**Framework**: Professional Video Applications  
**Kind**: class  
**Role**: Class

The `FxMatrix` class encapsulates a 4x4 matrix object and provides matrix inversion and transforming of 2D and 3D points.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
class FxMatrix44
```

```objc
@interface FxMatrix44 : NSObject
```

## Overview

> ❗ **Important**:  FxMatrix44 stores its data in *row major* order, which is different from OpenGL.

## Topics

### Creating and Initializing a Matrix
- [init!()](./fxmatrix44/init%28%29.md)
  Initializes the matrix to the identity matrix.
- [init!(fxMatrix: FxMatrix44!)](./fxmatrix44/init%28fxmatrix%29.md)
  Initializes the matrix using the specified matrix object.
- [init!(matrix44Data: UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./fxmatrix44/init%28matrix44data%29.md)
  Initializes a matrix with the specified data.
- [init!(colorMatrix44Data: UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./fxmatrix44/init%28colormatrix44data%29.md)
### Getting and Setting the Matrix
- [func setMatrix(UnsafeMutablePointer<(Double, Double, Double, Double)>!)](./fxmatrix44/setmatrix%28_%29.md)
  Sets the matrix to the specified values.
- [func matrix() -> UnsafeMutablePointer<Matrix44Data>!](./fxmatrix44/matrix%28%29.md)
  Gets the raw matrix data.
- [func setToIdentity()](./fxmatrix44/settoidentity%28%29.md)
  Sets the matrix to the identity matrix.
### Transforming the Matrix
- [func invert() -> Bool](./fxmatrix44/invert%28%29.md)
  Inverts the matrix if possible.
- [func invertColorMatrix(withTolerance: Double) -> Bool](./fxmatrix44/invertcolormatrix%28withtolerance%29.md)
  Inverts the matrix if possible.
- [func transpose()](./fxmatrix44/transpose%28%29.md)
  Transposes the matrix.
### Transforming Points Using the Matrix
- [func transform2DPoint(FxPoint2D) -> FxPoint2D](./fxmatrix44/transform2dpoint%28_%29.md)
  Transforms a 2D point using the matrix.
- [func transform3DPoint(FxPoint3D) -> FxPoint3D](./fxmatrix44/transform3dpoint%28_%29.md)
  Transforms a 3D point using the matrix.
### Constants
- [typealias Matrix44Data](./matrix44data.md)
  A matrix data type in the raw format.
### Initializers
- [init?(coder: NSCoder)](./fxmatrix44/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### 3D and lighting
- [protocol Fx3DAPI_v5](./fx3dapi_v5.md)
  An API that defines the methods the host application provides to get information about the 3D environment, including camera and object transforms.
- [protocol FxLightingAPI_v3](./fxlightingapi_v3.md)
  An API you use to get information about lights in a scene in a Motion project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxmatrix44)*