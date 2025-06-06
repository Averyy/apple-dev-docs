# translationInObject()

**Framework**: Watchkit  
**Kind**: method

The amount of translation for the pan gesture in the current object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func translationInObject() -> CGPoint
```

#### Return Value

A point representing the translation value relative to the current object’s coordinate system.

#### Discussion

The x and y values report the total translation over time. They are not delta values from the last time that the translation was reported.

## See Also

- [func velocityInObject() -> CGPoint](wkpangesturerecognizer/velocityinobject.md)
  The velocity of the pan gesture in the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/translationinobject())*