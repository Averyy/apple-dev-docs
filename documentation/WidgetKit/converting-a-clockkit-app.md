# Migrating ClockKit complications to WidgetKit

**Framework**: WidgetKit

Leverage WidgetKit’s API to create watchOS complications using SwiftUI.

#### Overview

With watchOS 9 and later, you can create complications for your watchOS app using SwiftUI views in WidgetKit. WidgetKit provides a modern API for creating and updating glanceable elements — making it an ideal fit for watchOS complications. Because WidgetKit’s design is inspired by ClockKit, if you’ve already designed ClockKit complications for your app, the process feels familiar. Similarly, if you’re already using widgets for iOS, you can quickly set up WidgetKit complications for a watchOS app. In many cases, you can use the same code to display WidgetKit complications in watchOS and widgets on the Lock Screen on iPhone. For more information, see [`Creating accessory widgets and watch complications`](creating-accessory-widgets-and-watch-complications.md).

##### Add Widgetkit to Your Project

To convert ClockKit complications to WidgetKit, start by adding a WidgetKit extension to your watchOS project.

![A screenshot showing the Widget Extension selected.](https://docs-assets.developer.apple.com/published/dd1b7749ddedf297c74e9186fac6b9d8/add-widgetkit-watchos%402x.png)

1. In Xcode, select the project icon in the Project navigator.
2. Click the “Add a target” button.
3. In the watchOS tab, select the Widget Extension template and click Next.
4. Give the new target a name.
5. If your app dynamically creates the set of [`CLKComplicationDescriptor`](https://developer.apple.com/documentation/ClockKit/CLKComplicationDescriptor) objects to support multiple complication types, enable the Include Configuration App Intent option. If you don’t plan to configure your complications using app intents, you can disable this option.
6. Click Finish.

Xcode creates a new target containing Swift files for the widget, an asset catalog, and an `Info.plist` file for the extension. The WidgetKit template provides you with structures that adopt the [`Widget`](https://developer.apple.com/documentation/SwiftUI/Widget) and [`View`](https://developer.apple.com/documentation/SwiftUI/View) protocols. It also includes a starting implementation for your [`TimelineProvider`](timelineprovider.md), or [`AppIntentTimelineProvider`](appintenttimelineprovider.md) if you enabled Include Configuration App Intent.

![A screenshot of a Widget Extension that contains support for custom app intent definitions: an intent timeline provider and custom app intent.](https://docs-assets.developer.apple.com/published/6a46262ff41eede6a9a280b8917e0884/configurable-complication-extension%402x.png)

> ❗ **Important**: After you add a WidgetKit extension to your project, the system tries to use it to generate complications for your watchOS app. As soon as your WidgetKit extension begins providing widget-based complications, the system disables your app’s ClockKit complications. It no longer wakes your app to call your [`CLKComplicationDataSource`](https://developer.apple.com/documentation/ClockKit/CLKComplicationDataSource) object’s methods to request timeline entries. However, the system may still wake your data source to call [`getWidgetConfiguration(from:completionHandler:)`](https://developer.apple.com/documentation/ClockKit/CLKComplicationWidgetMigrator/getWidgetConfiguration(from:completionHandler:)), while migrating complications from ClockKit to WidgetKit.

##### Configure Your Timeline Provider

The template creates a `Provider` structure that adopts the `TimelineProvider` or `AppIntentTimelineProvider` protocol, and provides a default implementation for the protocol’s methods. WidgetKit calls these methods to get the data needed to create the widget view.

> **Note**: WidgetKit’s daily budget for reloading the timeline works differently than ClockKit’s. Your widget-based complication receives up to 75 updates per day, based on how often they’re viewed. If you have a complication on the Apple Watch face, it’s always considered viewed, so your budget tends towards the higher end of that range.

In each of the protocol methods, your app needs to create and return one or more [`TimelineEntry`](timelineentry.md) instances:

The template provides a timeline entry that contains the date when the system should display it. Add any extra properties that you need for your complications.

```swift
struct CoffeeTrackerEntry: TimelineEntry {
    let date: Date
    let mgCaffeine: Double
    let totalCups: Double
}
```

Then, begin updating the timeline provider’s methods. For the placeholder, the system automatically redacts all of the widget’s content, unless you explicitly mark items with the [`unredacted()`](https://developer.apple.com/documentation/SwiftUI/View/unredacted()) view modifier in your complication’s SwiftUI view. As a result, you may want to provide generic data that fills out the redacted version.

```swift
func placeholder(in context: Context) -> SimpleEntry {
    
    // Show a complication with generic data.
    CoffeeTrackerEntry(date: Date(),
                       mgCaffeine: 250.0,
                       totalCups: 2.0)
}
```

The system can display the placeholder when the watch is locked, when it’s in Always On mode, and when it can’t otherwise display a live version of your complication.

For the snapshot, return a single entry. In general, you want to return the current state of your app. However, the system also uses the snapshot when displaying your complication in the complication picker. When returning your snapshot entry, be sure to check the `context` parameter [`isPreview`](timelineprovidercontext/ispreview.md) property. This property indicates whether the snapshot will be used in the complication picker. If this is `true`, provide generic data that shows your app’s typical appearance.

```swift
func getSnapshot(in context: Context, completion: @escaping (CoffeeTrackerEntry) -> Void) {
    
    if context.isPreview {
        // Show a complication with generic data.
        let entry = CoffeeTrackerEntry(date: Date(),
                    mgCaffeine: 250.0,
                    totalCups: 2.0)
        
        completion(entry)
        return
    }
    
    Task {
        
        let date = Date()
        
        // Get the current data from the model.
        let mgCaffeine = await data.mgCaffeine(atDate: date)
        let totalCups = await data.totalCupsToday
        
        // Create the entry.
        let entry = CoffeeTrackerEntry(date: date,
                                mgCaffeine: mgCaffeine,
                                totalCups: totalCups)
        
        // Pass the entry to the completion handler.
        completion(entry)
    }
}
```

For the timeline, create an array of entries, and then create a [`Timeline`](timeline.md) instance from that array. You can also select a reload policy for the timeline. By default, the system reloads the timeline when you reach its end. However, in the example below, the system only reloads the timeline when you explicitly request it.

```swift
func getTimeline(in context: Context, completion: @escaping (Timeline<Entry>) -> Void) {
    Task {

        // Create an array to hold the events.
        var entries: [CoffeeTrackerEntry] = []
        
        // The total number of cups consumed only changes when the user actively adds a drink,
        // so it remains constant in this timeline.
        let totalCups = await data.totalCupsToday

        // Generate a timeline covering every 5 minutes for the next 24 hours.
        let currentDate = Date()
        for minuteOffset in stride(from: 0, to: 60 * 24, by: 5) {
            let entryDate = Calendar.current.date(byAdding: .minute, value: minuteOffset, to: currentDate)!
            
            // Get the projected data for the specified date.
            let mgCaffeine = await data.mgCaffeine(atDate: entryDate)
            
            // Create the entry.
            let entry = CoffeeTrackerEntry(date: entryDate,
                                           mgCaffeine: mgCaffeine,
                                           totalCups: totalCups)
            
            // Add the event to the array.
            entries.append(entry)
        }

        // Create the timeline and pass it to the completion handler.
        // Because the caffeine dose drops to 0.0 mg after 24 hours,
        // there's no need to reload this timeline unless the user adds
        // a new drink. Setting the reload policy to .never.
        let timeline = Timeline(entries: entries, policy: .never)
        
        // Pass the timeline to the completion handler.
        completion(timeline)
    }
}
```

For more information, see [`Making a configurable widget`](making-a-configurable-widget.md) and [`Keeping a widget up to date`](keeping-a-widget-up-to-date.md).

##### Support Multiple Complications

If your app provides a static set of widgets, you can define multiple widgets using a [`WidgetBundle`](https://developer.apple.com/documentation/SwiftUI/WidgetBundle) protocol. For example, the code listing below provides three complications: one that displays the user’s current caffeine dose, one that provides the total number of cups of coffee for the day, and one that provides both. Each widget can then support a different subset of the available families.

```swift
@main
struct CoffeeTrackerWidgets: WidgetBundle {
   var body: some Widget {
       CaffeineComplication()
       CupsComplication()
       CaffeineAndCupsComplication()
   }
}
```

However, if you need to dynamically configure a set of complications, provide a custom app intent. For example, a weather app may let people install complications for any cities in their favorites list.

WidgetKit uses app intents for customizable properties, the same method that Siri Suggestions and Siri Shortcuts use to customize those interactions. In iOS, the app intents describe elements that the user can customize. For WidgetKit complications in watchOS, these intents aren’t user configurable. Instead, they represent items that your app can dynamically configure.

To customize the widgets, implement your [`AppIntentTimelineProvider`](appintenttimelineprovider.md) structure’s [`recommendations()`](appintenttimelineprovider/recommendations().md) method to return an array of [`AppIntentRecommendation`](appintentrecommendation.md) instances.

```swift
func recommendations() -> [AppIntentRecommendation<ConfigurationAppIntent>] {
    var recommendations = [AppIntentRecommendation<ConfigurationAppIntent>]()
    
    for cityID in favoriteCityIDs {
        let intent = ConfigurationAppIntent()
        intent.cityID = cityID
        recommendations.append(AppIntentRecommendation(intent: intent, description: cityName(id: cityID)))
    }

    return recommendations
}
```

For more information, see [`Making a configurable widget`](making-a-configurable-widget.md).

##### Design the Complication Using Swiftui

Use SwiftUI static views, such as text, shapes, or images, to create your complication’s content. You can also add render effects like blurs and gradients, but keep in mind that complications only have one or two frames in which to render the effect.

Because complications show a snapshot of the app’s data at a particular point in time, they don’t support features like animation. Additionally, if the user touches your complication, the system launches your app instead of passing the touch event to the SwiftUI views, so a complication can’t use interactive elements like buttons or switches.

Start by updating your [`Widget`](https://developer.apple.com/documentation/SwiftUI/Widget) structure.

```swift
struct CaffeineComplication: Widget {
    
    // Create a unique string to identify the complication.
    let kind: String = "com.example.caffeine-complication"

    var body: some WidgetConfiguration {
        StaticConfiguration(kind: kind, provider: Provider()) { entry in
            CoffeeTrackerComplicationsEntryView(entry: entry)
        }
        .configurationDisplayName("Coffee Tracker")
        .description("Shows the current caffeine dose in your system.")
        .supportedFamilies([.accessoryCorner, .accessoryCircular, .accessoryInline])
    }
}
```

The body of the widget contains either a static or intent configuration, depending on whether your app uses custom app intent definitions. Use the configuration to set items like the complication’s display name and the supported families. The configuration also takes a closure that returns a SwiftUI view for the specified entry.

WidgetKit reduces the number of families you need to support. In some cases, a WidgetKit accessory family covers more than one ClockKit family, which reduces the number of supported families from 12 to 4.

| ClockKit family | WidgetKit family |
| --- | --- |
| [`CLKComplicationFamily.graphicRectangular`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/graphicRectangular) | [`WidgetFamily.accessoryRectangular`](widgetfamily/accessoryrectangular.md) |
| [`CLKComplicationFamily.graphicCorner`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/graphicCorner) | [`WidgetFamily.accessoryCorner`](widgetfamily/accessorycorner.md) |
| [`CLKComplicationFamily.graphicCircular`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/graphicCircular), [`CLKComplicationFamily.graphicBezel`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/graphicBezel), [`CLKComplicationFamily.graphicExtraLarge`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/graphicExtraLarge) | [`WidgetFamily.accessoryCircular`](widgetfamily/accessorycircular.md) |
| [`CLKComplicationFamily.utilitarianSmallFlat`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/utilitarianSmallFlat), [`CLKComplicationFamily.utilitarianLarge`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/utilitarianLarge) | [`WidgetFamily.accessoryInline`](widgetfamily/accessoryinline.md) |

> **Note**: watchOS 9 and later no longer shows families like [`CLKComplicationFamily.circularSmall`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/circularSmall), [`CLKComplicationFamily.modularSmall`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/modularSmall), or [`CLKComplicationFamily.modularLarge`](https://developer.apple.com/documentation/ClockKit/CLKComplicationFamily/modularLarge) on watch faces.

Use the [`widgetFamily`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/widgetFamily) environment value to determine the complication’s family. You can provide a different SwiftUI view for each family. You can also get the family from the context passed to your timeline provider’s [`getTimeline(in:completion:)`](timelineprovider/gettimeline(in:completion:).md), [`getSnapshot(in:completion:)`](timelineprovider/getsnapshot(in:completion:).md), and [`placeholder(in:)`](timelineprovider/placeholder(in:).md) methods.

```swift
struct CaffeineComplicationView: View {
    
    // Get the widget's family.
    @Environment(\.widgetFamily) private var family
    
    var entry: Provider.Entry
    
    var body: some View {
        switch family {
        case .accessoryCircular:
            MyCircularComplication(mgCaffeine: entry.mgCaffeine,
                                   totalCups: entry.totalCups)
            
        case .accessoryCorner:
            MyCornerComplication(mgCaffeine: entry.mgCaffeine,
                                 totalCups: entry.totalCups)
            
        case .accessoryInline:
            MyInlineComplication(mgCaffeine: entry.mgCaffeine,
                                 totalCups: entry.totalCups)
            
        default:
            Image("AppIcon")
        }
    }
}
```

Then, check the [`WidgetRenderingMode`](widgetrenderingmode.md) environmental value to determine whether your complication is rendered in full color or using accent colors. Modify your design to best suit the current rendering mode.

```swift
struct MyCircularComplication: View {
    // Get the rendering mode.
    @Environment(\.widgetRenderingMode) var renderingMode
    
    var mgCaffeine: Double
    var totalCups: Double
    let maxMG = 500.0
    
    var body: some View {
        Gauge( value: min(mgCaffeine, maxMG), in: 0.0...maxMG ) {
            Text("mg")
        } currentValueLabel: {
            if renderingMode == .fullColor {
                // Add a foreground color to the label.
                Text(mgCaffeine.formatted(myFloatFormatter))
                    .foregroundStyle(.doseColor(for: mgCaffeine))
            }
            else {
                // Otherwise, use the default text color.
                Text(mgCaffeine.formatted(myFloatFormatter))
            }
        }
        .gaugeStyle(
            // Add a gradient to the gauge.
            CircularGaugeStyle(tint: Gradient(stops: myStops)))
    }
}
```

In [`accented`](widgetrenderingmode/accented.md) mode, you can explicitly partition your view into an accented group and the default group by adding the [`widgetAccentable(_:)`](https://developer.apple.com/documentation/SwiftUI/View/widgetAccentable(_:)) view modifier to part of your complication’s view hierarchy. For more information, see [`Creating accessory widgets and watch complications`](creating-accessory-widgets-and-watch-complications.md) and [`Creating views for widgets, Live Activities, and watch complications`](creating-views-for-widgets-live-activities-and-watch-complications.md).

When designing your WidgetKit complications, build your complication views so that they can adapt to different sizes. For example, you can use [`ViewThatFits`](https://developer.apple.com/documentation/SwiftUI/ViewThatFits) to provide a set of different-sized views, letting the system pick the best fit for the current context.

You can add a standard background to your complication by adding a [`AccessoryWidgetBackground`](accessorywidgetbackground.md) in a [`ZStack`](https://developer.apple.com/documentation/SwiftUI/ZStack) behind your widget’s content, and you can also add additional information to circular and corner complications using a [`widgetLabel(label:)`](https://developer.apple.com/documentation/SwiftUI/View/widgetLabel(label:)). Use the widget label to add gauges, progress views, or text along the inside curve of the corner view, or to add an image and text along the bezel of the Infograph watch face.

Finally, consider how Always On affects your complications. You may need to redact sensitive information, or adjust the widget’s appearance for reduced luminance. You can explicitly redact sensitive information using the [`privacySensitive(_:)`](https://developer.apple.com/documentation/SwiftUI/View/privacySensitive(_:)) view modifier. If you do, the system displays the redacted version of your view during Always On. For more information, see [`Designing your app for the Always On state`](https://developer.apple.com/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state).

> **Note**: If you don’t use the [`privacySensitive(_:)`](https://developer.apple.com/documentation/SwiftUI/View/privacySensitive(_:)) view modifier anywhere in your view hierarchy, the system displays a placeholder instead of a live complication. By default, the placeholder redacts all of your complication’s content.

#### Migrate Complications on a Watch Face

When users upgrade your app, you need to transition them from the old ClockKit complications to your new WidgetKit complications. Start by implementing your [`CLKComplicationDataSource`](https://developer.apple.com/documentation/ClockKit/CLKComplicationDataSource) type’s [`widgetMigrator`](https://developer.apple.com/documentation/ClockKit/CLKComplicationDataSource/widgetMigrator) method. Use your implementation to return an instance that conforms to the [`CLKComplicationWidgetMigrator`](https://developer.apple.com/documentation/ClockKit/CLKComplicationWidgetMigrator) protocol.

For example, update your data source so that it conforms to the [`CLKComplicationWidgetMigrator`](https://developer.apple.com/documentation/ClockKit/CLKComplicationWidgetMigrator) protocol.

```swift
class ComplicationController: NSObject, CLKComplicationDataSource, CLKComplicationWidgetMigrator {
   // ...
}
```

Then, have the [`widgetMigrator`](https://developer.apple.com/documentation/ClockKit/CLKComplicationDataSource/widgetMigrator) property return `self`.

```swift
var widgetMigrator: CLKComplicationWidgetMigrator {
    self
}
```

Finally, implement the [`getWidgetConfiguration(from:completionHandler:)`](https://developer.apple.com/documentation/ClockKit/CLKComplicationWidgetMigrator/getWidgetConfiguration(from:completionHandler:)) method. This method determines the best WidgetKit configuration for the given complication descriptor. This example uses the Swift async version of the method:

```swift
func widgetConfiguration(from complicationDescriptor: CLKComplicationDescriptor) async -> CLKComplicationWidgetMigrationConfiguration? {
    
    switch complicationDescriptor.identifier {
    case caffeineDoseIdentifier:
        return CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "com.example.Caffeine-Complication",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")

    case cupTotalIdentifier:
        return CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "com.example.CupTotal-Complication",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")

    case cupAndCaffeineIdentifier:
        return CLKComplicationStaticWidgetMigrationConfiguration(
            kind: "com.example.CupAndCaffeine-Complication",
            extensionBundleIdentifier: "com.example.apple-samplecode.Coffee-Tracker.watchkitapp.watchkitextension.CoffeeTracker-Complications")

    default:
        return nil
    }
}
```

## See Also

- [struct AccessoryWidgetGroup](accessorywidgetgroup.md)
  A view type that has a label at the top and three content views masked with a circle or rounded square.
- [struct AccessoryWidgetGroupStyle](accessorywidgetgroupstyle.md)
  The style for an [`AccessoryWidgetGroup`](accessorywidgetgroup.md) view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/converting-a-clockkit-app)*