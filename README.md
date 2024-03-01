# chargetime

This is a trivial program to quickly calculate when your car
will be charged to the target level using an AC charger.

# Use

```sh
cd chargetime
source chargetime.sh
chargetime {-c NN} [-opts]
```

options:

```bash
  -h, --help            show this help message and exit
  -b BATTERY_CAPACITY, --battery-capacity BATTERY_CAPACITY
                        Usable battery capacity in kWh. Defaults to 77.5 (Audi Q4 50)
  -c CURRENT_CHARGE, --current-charge CURRENT_CHARGE
                        Current charge level in percent
  --kw KW               Charger rating in kW. Defaults to 6.3
  -s START, --start START
                        The time when charging started. Defaults to five minutes ago.
  -t {10,20,30,40,50,60,70,80,90,100}, --target-charge {10,20,30,40,50,60,70,80,90,100}
                        Target charge level in percent. Defaults to 80.
```

You can change the defaults. We have a number of 6.3kW AC chargers at 
University of Richmond, and that is the reason for the default rating of
the charger. You can change it. 

The defaults for the target charge level, 80%, and the battery capacity, 77.5kWh,
are the values for my car. You can change those as well. The default start time
is not "now," but five minutes ago because the typical use case is hooking up
the charger, and then walking to my office. 
