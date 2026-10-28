# Handling User Activity

**Framework**: WatchKit  
**Role**: Article

Detect and respond to user activity information from Handoff or a complication.

## Overview

SwiftUI provides the [`onContinueUserActivity(_:perform:)`](../SwiftUI/view/oncontinueuseractivity%28_,perform%29.md) modifier to handle incoming [`NSUserActivity`](../Foundation/nsuseractivity.md) objects. This replaces the WatchKit extension delegate’s [`handle(_:)`](./wkextensiondelegate/handle%28_%29-5pyj1.md) method.

For example, if you create a complication descriptor using the [`init(identifier:displayName:supportedFamilies:userActivity:)`](../ClockKit/clkcomplicationdescriptor/init%28identifier,displayname,supportedfamilies,useractivity%29.md) initializer to pass in an [`NSUserActivity`](../Foundation/nsuseractivity.md) object, when the user taps the corresponding complication, the system activates your app and passes the activity object to your [`onContinueUserActivity(_:perform:)`](../SwiftUI/view/oncontinueuseractivity%28_,perform%29.md) modifiers. You can use the activity object to navigate to the corresponding content in your app.

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

### Responding to life cycle events
- [Handling Common State Transitions](./handling-common-state-transitions.md)
  Detect and respond to common state transitions.
- [Working with the watchOS app life cycle](./working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [Taking advantage of frontmost app state](./taking-advantage-of-frontmost-app-state.md)
  Understand the frontmost app state, and the features it provides to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/handling-user-activity)*