# removeObserver(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Removes a display configuration change observer.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func removeObserver(_ observer: any VZGraphicsDisplayObserver)
```

```objc
- (void) removeObserver:(id<VZGraphicsDisplayObserver>) observer;
```

## Parameters

- `observer`: The observer to remove from notifications about display configuration changes.

## See Also

### Observing changes to the display configuration
- [func addObserver(any VZGraphicsDisplayObserver)](./addobserver%28_%29.md)
  Adds an observer to notify about display configuration changes.
- [protocol VZGraphicsDisplayObserver](../vzgraphicsdisplayobserver.md)
  A protocol you implement to observe state changes in graphic displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/removeobserver(_:))*