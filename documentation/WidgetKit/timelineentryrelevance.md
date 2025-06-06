# TimelineEntryRelevance

**Framework**: Widgetkit  
**Kind**: struct

An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
struct TimelineEntryRelevance
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)

#### Overview

When users put widgets into a stack, WidgetKit uses the [`relevance`](timelineentry/relevance.md) property of the entries your timeline provider generates to determine how relevant they are to the user. For each timeline entry that your provider creates, you may assign relevance that contains a [`score`](timelineentryrelevance/score.md) and a [`duration`](timelineentryrelevance/duration.md). The score is a value you choose that indicates the relevance of the widget, relative to entries across timelines that the provider creates. When the date of an entry arrives, and for the duration you specify, WidgetKit may rotate your widget to the top of the stack so it becomes visible.

For example, consider a widget that displays stock market information. During open market hours, the widget is more relevant than when the market is closed. Additionally, a stock in the user’s watchlist is more relevant than stocks not in the watchlist. As a result, the score for entries during market hours is higher, and the score for entries displaying watchlist stocks could be even higher.

A different example might be a widget that displays a game character’s health level. During the time that the health level is recovering, it may be more relevant than when it has reached 100 percent. Conversely, you might decide that a character’s widget is less relevant until its health level reaches 100 percent. Only you can determine how relevant a widget’s content is to the user.

##### Adding Relevance to Timeline Entries

When you can determine the relative importance of timeline entries, set the `relevance` property on the entries you create. WidgetKit maintains the relevance information across multiple timelines, for the duration you specify. After generating a timeline entry with a relevance containing a positive score, if you create subsequent timelines and want to maintain the original relevance, set the `relevance` property to `nil`. To remove a previous relevance, or to specify that WidgetKit not consider rotating a widget to the top of a stack, set the `relevance` property’s score to zero (0).

For example, the stock market widget might create a timeline with a single entry at the opening of the market. This entry would include `TimelineEntryRelevance`, with the appropriate relevance score and a duration, in seconds, up to the closing of the market. For subsequent timelines, until the closing of the market, `relevance` is set to `nil`. This value indicates that the previous relevance, set at the opening of the market, should be maintained. When the provider generates a timeline at the close of the market, it includes a new `relevance`, with a score of 0 and a duration up to the next market opening time. These values indicate that the widget is no longer relevant and shouldn’t be promoted to the top of the stack.

##### Calculating a Score

To determine a score for an individual entry, it’s preferable to decide on an absolute scale from least relevant to most relevant. The range of the scale is entirely up to you and could be 1 to 100, 50 to 5000, or any other range of positive numbers that’s meaningful to you. WidgetKit calculates the relative difference of scores between entries, so the absolute values don’t matter.

Because WidgetKit maintains relevance information across timelines, you should use a consistent scale for all of them. For simplicity, you might use an enumeration with specific values for `low`, `medium`, and `high` relevance. Alternatively, if your score calculations have a continuous variation, you could use floating-point precision in your scale, with consistent minimum and maximum values.

A score of zero (0) or lower indicates that a widget is not relevant, and WidgetKit won’t consider rotating it to the top of the stack.

##### Testing Widgets in Stacks

When a widget is in a stack, and the user enables Smart Rotate for the stack, WidgetKit normally limits the number of times it considers rotating the widget to the top of the stack. To bypass this limit during development, enable the WidgetKit Developer Mode switch in Settings > Developer.

## Topics

### Creating a Relevance Object
- [init(score: Float, duration: TimeInterval)](timelineentryrelevance/init(score:duration:).md)
  Creates an object that represents the importance of a widget and the length of time for WidgetKit to consider it for rotation to the top of the stack.
### Configuring Relevance Properties
- [var duration: TimeInterval](timelineentryrelevance/duration.md)
  The number of seconds, following an entry’s date, that WidgetKit considers the widget for rotation to the top of the stack.
- [var score: Float](timelineentryrelevance/score.md)
  A value that indicates the relevance of an entry compared to other entries in the current and past timelines.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Donate intents and indicate relevance to automatically show your widget in Smart Stacks when it has useful information to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineentryrelevance)*