# Increasing the visibility of widgets in Smart Stacks

**Framework**: Widgetkit

Donate intents and indicate relevance to automatically show your widget in Smart Stacks when it has useful information to display.

#### Overview

Smart Stacks efficiently organize multiple widgets on the Home Screen to show useful content at just the right time. For example, if a person checks the daily weather forecast every morning, or if they frequently check the charges a family member makes on a joint credit card, then with input from your app, on-device intelligence can identify these patterns, enabling Smart Stacks to show and suggest the corresponding widgets at the right moments.

When people configure Smart Stacks, they have two options for surfacing widgets:

- Smart Rotate automatically rotates widgets to the top of the stack when they have timely, relevant information to show.
- Widget Suggestions automatically propose widgets that a person doesn’t already have in their stack, perhaps exposing them to widgets they don’t even know exist.

Smart Stacks use information from your app and widget extension to detect patterns of usage, and to promote or suggest widgets in a Smart Stack. Your app donates intents and identifies relevant shortcuts to provide a signal about how people use your app, when they use it, and what is most relevant to them. Your widget extension’s timeline entry provider generates timeline entries that contain hints about the relative importance of the widget’s content over time.

##### Use App Intents to Tell the System How People Use Your App

When you donate app intents, the system learns how and when people interact with your app. These donations inform much more than Smart Stacks. The system uses this information to display Spotlight search results, offer shortcuts on the Lock Screen and Siri watch face, and more. For more information about donating app intents, see [`Intent discovery`](https://developer.apple.com/documentation/AppIntents/intent-discovery).

For widgets based on [`AppIntentConfiguration`](appintentconfiguration.md), your app uses [`IntentDonationManager`](https://developer.apple.com/documentation/AppIntents/IntentDonationManager) or [`donate()`](https://developer.apple.com/documentation/AppIntents/AppIntent/donate()-1e60c) to inform Smart Rotate and Widget Suggestions in Smart Stacks. When your app donates an `AppIntent`, Smart Stacks consider rotating matching widgets to the top, or inserting an automatically configured widget as a suggestion.

Consider a tour guide app that displays information for cities around the world, such as popular tourist attractions, restaurants, and upcoming festivals throughout the year. The app contains several widgets that display these details. The widget configurations define custom intents such as `CityInfoAppIntent`, `AttractionAppIntent`, `RestaurantAppIntent`, and `FestivalAppIntent`. As people interact with the app, the app donates these app intents using `donate()`. The system uses the details of the app intents when determining user intention.

For example, a person frequently uses a travel app on the weekend to plan a trip to France. As they use the app, they look for festivals in various cities they may visit. Each time they search for or view the details of a festival, the app donates a `FestivalAppIntent`. If the `FestivalAppIntent` contains `location` and `type` parameters, the system can learn that the person frequently searches for art events in Paris. Your app’s donations give the system insight into the person’s behavior and what information is important to them.

To make relevant suggestions, Smart Stacks compare app intents the app donates with app intents that configurable widgets use. If a person configures a widget that uses a `FestivalAppIntent` to show art festivals in Paris, Smart Stacks can automatically rotate to that widget when the person typically looks for that information. If the person hasn’t configured a matching widget in a stack, the system can automatically suggest a widget with that configuration. This raises the visibility of the app’s widgets, which they may not know about.

> **Note**: To enable Smart Stacks to suggest your app intent-based widgets, have your custom app intents conform to [`PredictableIntent`](https://developer.apple.com/documentation/AppIntents/PredictableIntent) and contain a [`predictionConfiguration`](https://developer.apple.com/documentation/AppIntents/PredictableIntent/predictionConfiguration) that describes the parameters to match.

To enable Smart Stacks to suggest your app intent-based widgets, have your custom app intents conform to [`PredictableIntent`](https://developer.apple.com/documentation/AppIntents/PredictableIntent) and contain a [`predictionConfiguration`](https://developer.apple.com/documentation/AppIntents/PredictableIntent/predictionConfiguration) that describes the parameters to match.

##### Suggest Shortcuts a Person May Find Useful

While app intent donations using `IntentDonationManager` or `donate()` give Smart Stacks insight into past user behavior, [`RelevantIntent`](https://developer.apple.com/documentation/AppIntents/RelevantIntent) informs future suggestions. These app intents may not even be based on a person’s behavior. When your app has timely information you believe is relevant to a person, and the app has a widget to display that information, suggest relevant app intents to influence Widget Suggestions. This helps people perform common or important tasks.

Continuing the previous example, when the app receives details about a new outdoor art lantern festival in Paris, it can convey this new, likely relevant information to the system. Because the on-device intelligence has learned the person is interested in art festivals in Paris, it may suggest an app intent-based widget from the app that displays art festivals in a Smart Stack. The Smart Stack uses the app intent from the app to automatically configure the widget to show the details of the outdoor art lantern festival.

The app uses a `RelevantIntent` that contains the festival details. Because the new festival is in the future, Smart Stacks need to know when the app intent is relevant. The app conveys this information by specifying a  as part of the `RelevantIntent`. The relevant context determines when an app intent is relevant, such as at a specific time of day or location. To specify when it’s appropriate to suggest a widget in a Smart Stack, call [`updateRelevantIntents(_:)`](https://developer.apple.com/documentation/AppIntents/RelevantIntentManager/updateRelevantIntents(_:)) and pass one or more `RelevantIntent` objects. On-device intelligence uses the combination of the relevant app intent and the date details from the relevant context to make a widget suggestion at the right time.

To provide a relevant app intent with a `FestivalAppIntent` for the Paris art lantern festival, the app does the following:

1. Creates a `FestivalAppIntent` for the lantern festival with the `location` set to Paris and the `type` set to `Art`
2. Creates a `RelevantIntent` with the `FestivalAppIntent`, the widget’s kind string, and a [`RelevantContext`](https://developer.apple.com/documentation/AppIntents/RelevantContext) that specifies the start and end dates of the festival
3. Calls `updateRelevantIntents()` with the `RelevantIntent`

With this information, Smart Stacks can suggest the preconfigured lantern festival widget with no user action.  The person may not be aware that the app contains widgets, providing a great way for people to discover new features and interactions with your app.

If your widget uses a [`StaticConfiguration`](staticconfiguration.md), you still use `RelevantIntent` for future suggestions. To provide a relevant intent for a static widget, create a custom intent type that conforms to `WidgetConfigurationIntent` and has no parameters, then follow the steps above.

> **Note**: Smart Stacks don’t suggest widgets that rely on a person’s location information unless that person has already authorized the use of location for widgets in a widget extension. For more information about using a person’s location in widgets, see [`Accessing location information in widgets`](accessing-location-information-in-widgets.md).

Smart Stacks don’t suggest widgets that rely on a person’s location information unless that person has already authorized the use of location for widgets in a widget extension. For more information about using a person’s location in widgets, see [`Accessing location information in widgets`](accessing-location-information-in-widgets.md).

##### Indicate When a Widget Is Relevant From Your Widget Extension

Similar to how a `RelevantIntent` gives Smart Stacks insight into future relevant information, the widget timeline providers you implement in your widget extension specify relevance for future widget updates. After a person adds a widget to the Home Screen, the widget’s timeline provider generates timelines to populate the widget. As it generates timelines, the provider indicates the relative importance of entries over time by setting the [`relevance`](timelineentry/relevance.md) property on the timeline entries. Timeline providers can specify relevance to both static and app intent-based widget configurations.

For example, if a person adds the festival tracker widget to the Home Screen, the provider might indicate a relevance score of `1` for an upcoming festival in Paris because the person browsed festivals in Paris. If the person adds the lantern festival widget from the previous example and marks it as a favorite, the timeline provider might change the relevance score for those timeline entries from `1` to `10` to indicate a significantly more relevant entry. Smart Stacks consider the changes in relevance across all of a widget’s timeline entries when deciding to automatically rotate to that widget in a Smart Stack.

For more information about using relevance in timeline entries and providing relevance scores, see [`TimelineEntryRelevance`](timelineentryrelevance.md).

##### Test Widgets in Stacks

When a widget is in a stack, WidgetKit normally limits the number of times it considers rotating the widget to the top of the stack or inserting the widget as a suggestion. To bypass this limit during development, enable the WidgetKit Developer Mode switch in Settings > Developer.

For additional tips about debugging widgets, see [`Debugging Widgets`](debugging-widgets.md).

##### Provide Backward Compatibility

Prior to iOS 17, macOS 14, and watchOS 10, widgets used SiriKit Intents to make donations and to indicate relevance. For details about supporting older operating system versions, see [`Migrating widgets from SiriKit Intents to App Intents`](migrating-from-sirikit-intents-to-app-intents.md).

Donating SiriKit Intents is very similar to donating app intents. Instead of using `IntentDonationManager`, you use [`INInteraction`](https://developer.apple.com/documentation/Intents/INInteraction) to donate an [`INIntent`](https://developer.apple.com/documentation/Intents/INIntent). For more information about donating SiriKit Intents, see [`Donating Shortcuts`](https://developer.apple.com/documentation/SiriKit/donating-shortcuts) and [`Watch and Widget Support`](https://developer.apple.com/documentation/SiriKit/watch-and-widget-support).

## See Also

- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks)*