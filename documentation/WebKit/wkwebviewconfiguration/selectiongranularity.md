# selectionGranularity

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The level of granularity with which the user can interactively select web view content.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This property is ignored; selection granularity is always `character`.

## Declaration

```swift
var selectionGranularity: WKSelectionGranularity { get set }
```

```objc
@property (nonatomic) WKSelectionGranularity selectionGranularity;
```

#### Discussion

The value is one of the constants of the enumerated type [`WKSelectionGranularity`](../wkselectiongranularity.md). The default value is [`WKSelectionGranularity.dynamic`](../wkselectiongranularity/dynamic.md).

## See Also

### Setting selection granularity
- [enum WKSelectionGranularity](../wkselectiongranularity.md)
  The granularity with which the user can select and modify web view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/selectiongranularity)*