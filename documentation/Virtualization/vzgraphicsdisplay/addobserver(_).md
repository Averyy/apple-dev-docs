# addObserver(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Adds an observer to notify about display configuration changes.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func addObserver(_ observer: any VZGraphicsDisplayObserver)
```

```objc
- (void) addObserver:(id<VZGraphicsDisplayObserver>) observer;
```

## Parameters

- `observer`: The new observer the framework notifies about display configuration changes.

## See Also

### Observing changes to the display configuration
- [func removeObserver(any VZGraphicsDisplayObserver)](./removeobserver%28_%29.md)
  Removes a display configuration change observer.
- [protocol VZGraphicsDisplayObserver](../vzgraphicsdisplayobserver.md)
  A protocol you implement to observe state changes in graphic displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzgraphicsdisplay/addobserver(_:))*