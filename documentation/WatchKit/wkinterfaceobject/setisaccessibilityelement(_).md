# setIsAccessibilityElement(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the object is an accessibility element that an assistive app can access.

**Availability**:
- watchOS

## Declaration

```swift
func setIsAccessibilityElement(_ isAccessibilityElement: Bool)
```

```objc
- (void) setIsAccessibilityElement:(BOOL) isAccessibilityElement;
```

## Discussion

Use this method to change the accessibility status of your interface objects.

## Parameters

- `isAccessibilityElement`: [`true`](../../Swift/true.md) if the object is an accessibility element or [`false`](../../Swift/false.md) if it is not.

## See Also

### Configuring the Accessibility Attributes
- [func setAccessibilityIdentifier(String?)](./setaccessibilityidentifier%28_%29.md)
  Sets the unique identifier string for the interface object.
- [func setAccessibilityLabel(String?)](./setaccessibilitylabel%28_%29.md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](./setaccessibilityhint%28_%29.md)
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](./setaccessibilityvalue%28_%29.md)
  Sets the value of the accessibility element.
- [func setAccessibilityTraits(UIAccessibilityTraits)](./setaccessibilitytraits%28_%29.md)
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](./setaccessibilityimageregions%28_%29.md)
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setisaccessibilityelement(_:))*