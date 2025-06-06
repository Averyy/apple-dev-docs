# Showing a Pass on the Lock Screen

**Framework**: Walletpasses

Add information to your pass so the system can display it on the Lock Screen at a relevant time and place.

#### Overview

Make it easier for the user to access your pass by enabling the system to show it on the lock screen when it’s relevant. For example, show a gym membership card at the gym, or a boarding pass when it’s time to board the plane.

A pass can be relevant on a date, at a location, or both. Set a date by adding the `relevantDate` key to [`Pass`](pass.md) for boarding passes, event tickets, and generic passes.

Provide relevant locations for a pass by adding the `locations` array to [`Pass`](pass.md). Each location includes optional text with an explanation of why the pass is relevant. Coupons, store cards, and generic passes must provide locations if you added any other type of relevance information to the pass object.

The system displays the pass on the lock screen if both the date and any location matches. Passes with no locations display on the relevant date. Similarly, passes with no relevant date display when one of the locations matches.

The following code shows the date and location relevance information from a pass:

```other
{
    ...

    "locations" : [
        {"latitude" : 37.3229, "longitude" : -122.0323},
        {"latitude" : 37.3286, "longitude" : -122.0143},
        {
            "altitude" : 10.0,
            "latitude" : 37.331,
            "longitude" : -122.029,
            "relevantText" : "Store nearby on 3rd and Main."
        }
    ],
    "relevantDate" : "2014-12-05T09:00-08:00"
}
```

A pass can have only 10 relevant locations. If your pass needs more locations, such as a coupon for a chain of stores, start with the best ones. Update the pass to change the array of relevant locations. For more information updating a pass, see `Distribute and Update a Pass`.

> **Note**:  Test your pass relevancy settings on a device. Simulator doesn’t show passes on the lock screen.

##### Add Relevancy with Ibeacons

Show your pass on the lock screen when the device comes close to an iBeacon. Add up to ten different UUIDs for iBeacons to the `beacons` array of the [`Pass`](pass.md) object.

The system uses a combination of the UUID, and the major and minor Bluetooth identifiers to determine beacon relevancy. To include more than ten beacons in the array, use the UUID to group the beacons and give each beacon in a group a different major and minor Bluetooth identifier.

The following code shows a pass with one beacon:

```other
{
   ...

   "beacons": [
      {
         "proximityUUID":"F8F589E9-C07E-58B0-AEAB-A36BE4D48FAC",
         "relevantText":"You're near my store",
         "name" : "My Store"
      }
   ]
}

```

## See Also

- [object Pass.Locations](pass/locations-data.dictionary.md)
  An object that represents a location that the system uses to show a relevant pass.
- [object Pass.Beacons](pass/beacons-data.dictionary.md)
  An object that represents the identifier of a Bluetooth Low Energy beacon the system uses to show a relevant pass.
- [object Pass.RelevantDates](pass/relevantdates-data.dictionary.md)
  An object that represents a date interval that the system uses to show a relevant pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletPasses/showing-a-pass-on-the-lock-screen)*