# HomeAccessoryRangeSetting.TickLabelStyle.custom(_:)

**Framework**: HomeExtensions  
**Kind**: case  
**Role**: Case

Custom labels, one for each tick mark.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
case custom([LocalizedStringResource])
```

#### Discussion

Provide the labels in the same order as the tick marks. To leave a tick mark unlabeled, specify an empty string as its label. You can set at most 12 labels on a slider.

## See Also

### Label styles
- [HomeAccessoryRangeSetting.TickLabelStyle.automatic](./automatic.md)
  Labels that display each tick mark’s value, using the setting’s decimal precision.
- [HomeAccessoryRangeSetting.TickLabelStyle.hidden](./hidden.md)
  No tick labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesetting/ticklabelstyle/custom(_:))*