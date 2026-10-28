# isEqual(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns whether one custom parameter value is equal to another.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func isEqual(_ rightValue: any NSCopying & NSSecureCoding & NSObjectProtocol) -> Bool
```

```objc
- (BOOL) isEqual:(NSObject<NSCopying,NSSecureCoding> *) rightValue;
```

## Return Value

True if the two values are equal, false otherwise.

## Discussion

The host application will sometimes need to know whether two custom parameters are equivalent. When it needs to know that, it will call this method on one custom parameter object, and pass it the other as `rightValue`.

## Parameters

- `rightValue`: The value to the right of the equal sign in the equation (`leftValue` == `rightValue`).

## See Also

### Instance Methods
- [func interpolateBetween(any NSCopying & NSSecureCoding & NSObjectProtocol, withWeight: Float) -> any NSCopying & NSSecureCoding & NSObjectProtocol](./interpolatebetween%28_,withweight%29.md)
  Returns a new parameter value which has been calculated by interpolating between                 two key values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameterinterpolation_v2/isequal(_:))*