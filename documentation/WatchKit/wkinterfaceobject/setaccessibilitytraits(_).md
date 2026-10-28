# setAccessibilityTraits(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the combination of accessibility traits that best characterize the accessibility element.

**Availability**:
- watchOS

## Declaration

```swift
func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)
```

```objc
- (void) setAccessibilityTraits:(UIAccessibilityTraits) accessibilityTraits;
```

## Discussion

Use this method to change the accessibility traits associated with your interface objects.

## Parameters

- `accessibilityTraits`: The traits that characterize this element. For a list of traits and appropriate combinations, see [`UIAccessibilityTraits`](../../UIKit/uiaccessibilitytraits.md).

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
- [func setIsAccessibilityElement(Bool)](./setisaccessibilityelement%28_%29.md)
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](./setaccessibilityimageregions%28_%29.md)
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilitytraits(_:))*