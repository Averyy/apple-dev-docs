# invertColorMatrix(withTolerance:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Inverts the matrix if possible.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
func invertColorMatrix(withTolerance tolerance: Double) -> Bool
```

```objc
- (BOOL) invertColorMatrixWithTolerance:(double) tolerance;
```

## Return Value

[`true`](../../Swift/true.md) if the invert succeeded; otherwise [`false`](../../Swift/false.md).

## Parameters

- `tolerance`: A threshold for determining whether inversion is possible. If set to 0, then inversion will only fail if the determininant of the matrix is exactly 0.0.

## See Also

### Transforming the Matrix
- [func invert() -> Bool](./invert%28%29.md)
  Inverts the matrix if possible.
- [func transpose()](./transpose%28%29.md)
  Transposes the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxmatrix44/invertcolormatrix(withtolerance:))*