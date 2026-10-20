# setAccessibilityIdentifier(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the unique identifier string for the interface object.

**Availability**:
- watchOS

## Declaration

```swift
func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)
```

```objc
- (void) setAccessibilityIdentifier:(NSString *) accessibilityIdentifier;
```

#### Discussion

Use the identifier in this property to distinguish between different objects in your app. The identifier string is used solely for programmatic identity, as opposed to many other accessibility attributes.

## Parameters

- `accessibilityIdentifier`: A string containing the identifier of the element. Specify `nil` to clear the existing identifier.

## See Also

### Configuring the Accessibility Attributes
- [func setAccessibilityLabel(String?)](./setaccessibilitylabel%28_%29.md)
  Sets a succinct label on the object that identifies the accessibility element.
- [func setAccessibilityHint(String?)](./setaccessibilityhint%28_%29.md)
  Sets the description of what happens when performing an action on the accessibility element.
- [func setAccessibilityValue(String?)](./setaccessibilityvalue%28_%29.md)
  Sets the value of the accessibility element.
- [func setIsAccessibilityElement(Bool)](./setisaccessibilityelement%28_%29.md)
  Sets whether the object is an accessibility element that an assistive app can access.
- [func setAccessibilityTraits(UIAccessibilityTraits)](./setaccessibilitytraits%28_%29.md)
  Sets the combination of accessibility traits that best characterize the accessibility element.
- [func setAccessibilityImageRegions([WKAccessibilityImageRegion])](./setaccessibilityimageregions%28_%29.md)
  Marks portions of an image as separate accessible elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setaccessibilityidentifier(_:))*