# selectionGranularity

**Framework**: WebKit  
**Kind**: property

The level of granularity with which the user can interactively select web view content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var selectionGranularity: WKSelectionGranularity { get set }
```

#### Discussion

The value is one of the constants of the enumerated type [`WKSelectionGranularity`](wkselectiongranularity.md). The default value is [`WKSelectionGranularity.dynamic`](wkselectiongranularity/dynamic.md).

## See Also

- [enum WKSelectionGranularity](wkselectiongranularity.md)
  The granularity with which the user can select and modify web view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/selectiongranularity)*