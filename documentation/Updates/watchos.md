# watchOS updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to watchOS.

#### Overview

Browse notable changes in [watchOS apps](../watchOS-Apps/watchOS-Apps.md).

#### September 2024

##### Watch sizes

- Apple Watch Series 10 are larger and have a different aspect ratio than previous watches. The watch is 1mm larger than the Series 9 (42mm and 46mm), but the screen gains more width than height. Use [`scenePadding(_:)`](../SwiftUI/view/scenepadding%28_%29.md) to align text with the text margins, and [`ignoresSafeArea(_:edges:)`](../SwiftUI/view/ignoressafearea%28_,edges%29.md) to extend content beyond the watch’s safe area.

##### Shallow dives

- Apple Watch Series 10 supports the Shallow Depth and Pressure capability. Use [`CMWaterSubmersionManager`](../CoreMotion/cmwatersubmersionmanager.md) to start a shallow dive session, and [`underwaterDepth`](../HealthKit/hkquantitytypeidentifier/underwaterdepth.md) and [`waterTemperature`](../HealthKit/hkquantitytypeidentifier/watertemperature.md) to read depth and temperature samples from HealthKit.

#### June 2024

##### Water temperature

- Access water temperature data from swimming workouts. Apple Watch Ultra records [`waterTemperature`](../HealthKit/hkquantitytypeidentifier/watertemperature.md) samples during swimming workouts.

##### Double tap

- Specify which control responds to the double tap gesture using the [`handGestureShortcut(_:isEnabled:)`](../SwiftUI/view/handgestureshortcut%28_,isenabled%29.md) view modifier, passing [`primaryAction`](../SwiftUI/handgestureshortcut/primaryaction.md) as the parameter. Double tap can interact with any buttonlike controls, such as buttons or toggles.

##### Creating workouts

- Create custom pool swimming workouts with the [`HKWorkoutActivityType.swimming`](../HealthKit/hkworkoutactivitytype/swimming.md) activity.
- Set a distance-with-time goal for custom swimming workouts with the [`WorkoutGoal.poolSwimDistanceWithTime(_:_:)`](../WorkoutKit/workoutgoal/poolswimdistancewithtime%28_,_%29.md) goal.
- Provide a custom name to a workout step using the [`WorkoutStep`](../WorkoutKit/workoutstep.md) structure’s [`displayName`](../WorkoutKit/workoutstep/displayname.md).
- Preview workouts on Apple Watch using the [`workoutPreview(_:isPresented:)`](../SwiftUI/view/workoutpreview%28_,ispresented%29.md) view modifier.
- Set average power goals for cycling and running with [`PowerThresholdAlert`](../WorkoutKit/powerthresholdalert.md) and [`PowerRangeAlert`](../WorkoutKit/powerrangealert.md).
- Set pace goals for indoor running with the [`SpeedThresholdAlert`](../WorkoutKit/speedthresholdalert.md) and [`SpeedRangeAlert`](../WorkoutKit/speedrangealert.md) targets.

#### September 2023

- When someone performs a Double Tap gesture while viewing a notification on Apple Watch Series 9 or Apple Watch Ultra 2, the system invokes the first nondestructive action. A nondestructive action doesn’t include the [`destructive`](../UserNotifications/unnotificationactionoptions/destructive.md) option, and won’t delete user data or change the app irrevocably.

#### June 2023

- Use the new watchOS user interface design to simplify navigation, better use the Digital Crown, and enrich the app experience. For more information, see [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos) and [Creating an intuitive and effective UI in watchOS 10](../watchOS-Apps/creating-an-intuitive-and-effective-ui-in-watchos-10.md).
- Update your WidgetKit-based complications to take advantage of the Smart Stack on Apple Watch. People can scroll down to see relevant widgets directly on the watch face using the Digital Crown. For more information, see [Increasing the visibility of widgets in Smart Stacks](../WidgetKit/widget-suggestions-in-smart-stacks.md).
- Use curved text along the bevel or around the corners in WidgetKit-based complications.
- Add state preservation and restoration to watchOS apps. For more information, see [Preserving your app’s UI across launches](../UIKit/preserving-your-app-s-ui-across-launches.md).
- Use WorkoutKit to create goal, pacer, multisport, and fully custom interval workouts. Display a preview of the workout that shows the workout details, and sync workouts with a paired Apple Watch. For more information, see   [WorkoutKit](../WorkoutKit/WorkoutKit.md).
- Access batches of high-frequency accelerometer and device motion data during workouts. Use this data to analyze motion — such as a golf or baseball swing — after the action occurs. For more information, see [Core Motion](../CoreMotion/CoreMotion.md).
- Use Core Motion’s water submersion manager to monitor shallow dives on Apple Watch Ultra. For more information, see [Core Motion](../CoreMotion/CoreMotion.md).
- Support Bluetooth cycling sensors. People can pair power, cadence, and speed sensors to Apple Watch to enhance their cycling workouts. You can access this data using HealthKit for live and historical workouts.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/watchos)*