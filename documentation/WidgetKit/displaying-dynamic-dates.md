# Displaying dynamic dates in widgets

**Framework**: WidgetKit

Show up-to-date, time-based information in your widget even when it isn’t running.

#### Overview

Because your widget extension isn’t always running, you can’t directly update your widget’s content. Instead, WidgetKit renders your widget’s view on your behalf and displays the result. However, some SwiftUI views let you display content that continues updating while your widget is visible.

Using a [`Text`](https://developer.apple.com/documentation/swiftui/text) view in your widget, you can display dates and times that stay up to date onscreen. The following examples show the combinations available.

To display a relative time that updates automatically, use code similar to the example below:

```swift
let components = DateComponents(minute: 11, second: 14)
let futureDate = Calendar.current.date(byAdding: components, to: Date())!

Text(futureDate, style: .relative)
// Displays:
// 11 min, 14 sec

Text(futureDate, style: .offset)
// Displays:
// -11 minutes
```

Using the [`relative`](https://developer.apple.com/documentation/swiftui/text/datestyle/relative) style shows the absolute difference between the current date and time and the date specified, regardless of whether the date is in the future or the past. The [`offset`](https://developer.apple.com/documentation/swiftui/text/datestyle/offset) style shows the difference between the current date and time and the date specified, indicating dates in the future with a minus sign (`-`) prefix and dates in the past with a plus sign (`+`) prefix.

To display a timer that continues updating automatically, use code similar to the example below:

```swift
let components = DateComponents(minute: 15)
let futureDate = Calendar.current.date(byAdding: components, to: Date())!

Text(futureDate, style: .timer)
// Displays:
// 15:00
```

For dates in the future, the [`timer`](https://developer.apple.com/documentation/swiftui/text/datestyle/timer) style counts down until the current time reaches the specified date and time, and counts up when the date passes.

To display an absolute date or time, use code similar to the example below:

```swift
// Absolute Date or Time
let components = DateComponents(year: 2020, month: 4, day: 1, hour: 9, minute: 41)
let aprilFirstDate = Calendar.current(components)!

Text(aprilFirstDate, style: .date)
Text("Date: \(aprilFirstDate, style: .date)")
Text("Time: \(aprilFirstDate, style: .time)")

// Displays:
// April 1, 2020
// Date: April 1, 2020
// Time: 9:41AM
```

To display a time interval between two dates, use code similar to the example below:

```swift
let startComponents = DateComponents(hour: 9, minute: 30)
let startDate = Calendar.current.date(from: startComponents)!

let endComponents = DateComponents(hour: 14, minute: 45)
let endDate = Calendar.current.date(from: endComponents)!

Text(startDate ... endDate)
Text("The meeting will take place: \(startDate ... endDate)")

// Displays:
// 9:30AM-2:45PM
// The meeting will take place: 9:30AM-2:45PM
```

To show progress toward a future date without reloading your widget, use [`init(timerInterval:countsDown:)`](https://developer.apple.com/documentation/swiftui/progressview/init(timerinterval:countsdown:)), as follows:

```swift
let start = Date.now
let end = start.addingTimeInterval(60 * 15)

ProgressView(timerInterval: start...end, countsDown: false)
```

The progress view fills in automatically as time passes from the start of the date range to the end. Set `countsDown` to `true` to leave the progress view empty instead.

To pair the progress view with a numeric countdown, or to show a countdown on its own without reloading your widget, use [`init(timerInterval:pauseTime:countsDown:showsHours:)`](https://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)), as shown here:

```swift
Text(timerInterval: start...end, countsDown: true)
// Displays:
// 15:00
```

Provide a `pauseTime` to stop the timer at a specific date, such as when a countdown reaches zero.

## See Also

- [struct Text](../swiftui/text.md)
  A view that displays one or more lines of read-only text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/displaying-dynamic-dates)*