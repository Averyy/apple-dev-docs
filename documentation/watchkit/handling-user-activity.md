# Handling User Activity

**Framework**: Watchkit

Detect and respond to user activity information from Handoff or a complication.

#### Overview

SwiftUI provides the [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onContinueUserActivity(_:perform:)) modifier to handle incoming [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects. This replaces the WatchKit extension delegate’s [`handle(_:)`](wkextensiondelegate/handle(_:)-5pyj1.md) method.

For example, if you create a complication descriptor using the [`init(identifier:displayName:supportedFamilies:userActivity:)`](https://developer.apple.com/documentation/ClockKit/CLKComplicationDescriptor/init(identifier:displayName:supportedFamilies:userActivity:)) initializer to pass in an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object, when the user taps the corresponding complication, the system activates your app and passes the activity object to your [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onContinueUserActivity(_:perform:)) modifiers. You can use the activity object to navigate to the corresponding content in your app.

```swift
// Create a list of the user's favorite cities.
List(favoriteCities) { city in
    
    // Create a navigation link for each city.
    // Activate the link if it is for the selected city.
    NavigationLink(city.name,
                   destination: CityDetailView(city: city),
                   isActive: checkActive(city: city))
        
        .onContinueUserActivity(viewCityFromComplication) { activity in
            
            // App received a user activity object.
            // Check to see whether it has a city index in the userInfo dictionary.
            if let id = activity.userInfo?[cityIDKey] as? String {
                
                // Navigate to the specified city.
                selectedCity = allCities[id]
            }
            else {
                
                // Display the favorite city list.
                selectedCity = nil
            }
        }
}
```

Note that in this example, `selectedCity` is a state variable that holds a `City` instance. The `checkActive(city:)` method creates a binding that indicates whether the given city is the currently selected city.

```swift
@State var selectedCity: City? = nil

// Returns a binding that determines whether a given
// city is the currently selected city.
func checkActive(city: City) -> Binding<Bool> {
    Binding {
        selectedCity == city
    }
    set: {
        // If the binding is set to true, set the selected city
        // to the provided city.
        if $0 {
            selectedCity = city
        }
        // if the binding is set to false,
        // and the selected city is set to the provided city,
        // clear the selected city.
        else if selectedCity == city {
            selectedCity = nil
        }
    }
}
```

## See Also

- [Handling Common State Transitions](handling-common-state-transitions.md)
  Detect and respond to common state transitions.
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [Taking Advantage of Frontmost App State](taking-advantage-of-frontmost-app-state.md)
  Understand the frontmost app state, and the features it provides to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/handling-user-activity)*