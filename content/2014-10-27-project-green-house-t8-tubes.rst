Project 'Green' House #3: LED replacement lighting for straight T8 1.2m Tubes
#############################################################################

:category: Environmental
:tags: Green House, Green, Energy, Environment
:status: draft

In my previous posts (`1`_, `2`_), I've talked about replacing the various
round fluorescent tubes in my house over to LEDs.  In this post, I'll cover
the replacement of long, 1.2 metre, straight T8 fluorescent tubes and discuss
the interesting results I had in this space.

.. image:: |filename|./images/led-lights/IMG_3663.JPG
   :width: 300px
   :alt: Before, T8 tube present

.. image:: |filename|./images/led-lights/IMG_3665.JPG
   :width: 300px
   :alt: After, LED tube replacement

In my house, I have a total of just two of these T8 tubes, both located in my garage.
They're positioned in a "standard" fluorescent light fitting, exactly the same
as those you'd find in shopping centres, car parks, stadiums and the like.
Take a look at the photos and you'll recognise what I mean.  These fittings
originally had semi-clear diffuser covers over the lights; in my house, I've
managed to break one of these, leaving the tube "raw".

.. note::

   Please note that any information here is provided as a guide only and no
   warranties or responsibility is taken with regards to its usage.  For more
   information, see the `licence`_ page.


Replacement lights
==================

* 2 x 18w T8 1.2m frosted cool white tubes: Cost $35.88 AU on
  `eBay
  <http://www.ebay.com.au/itm/CREE-LED-T8-Light-tube-lamp-fluorescent-replacement-60cm-120cm-COOL-WARM-WHITE-/130975927686>`__

.. image:: |filename|./images/led-lights/IMG_3646.JPG
   :width: 300px
   :alt: LED lights delivered

.. image:: |filename|./images/led-lights/IMG_3650.JPG
   :width: 300px
   :alt: LED light driver up close

At the time, these were be the cheapest and most cost-effective lights to
purchase, being delivered with free postage.  I'd investigated other options,
such as direct delivery from China via AliExpress, but the cost was too
prohibitive and one seller simply refused to ship the items to me because they
were concerned regarding breakage.  So, the eBay route was the best option.

I'd thought hard about whether to choose the higher wattage lamps, the warmer
white colour or the clear plastic covering over the frosted.  In the end, I
settled on:

* Cool white
* 18W
* Frosted

as the above seemed to fit closest with what I currently had in my garage,
where the original light to be replaced lived.  Due to a mishap with the
original fluorescent light covering breaking, there is no longer a diffuser
covering one light, so this slightly influenced my decision in clear versus
frosted.  As for the colouring, cool white matches the current colouring
closest, since it's a garage.  Finally, the 18W rating was more an educated
guess than anything, and as it turns out, a good one, as the light is brighter
than the original tubes; it is thus sufficiently bright and I don't need to
waste more power.

These replacement tubes came securely packed and ready to go, and the quality
of the tubes feels solid.  I haven't opened them up to look at the internals
yet - I may do this one day, since more and more Chinese electronics are quite
slipshod in their construction.

Unlike the previous circular LED panels, these tubes have their driver built
into the tube, so installation is a matter of connecting the AC current to
both ends of the tube, ensuring the old ballast and starter are removed, and
adjusting the wiring in accordance with what the new LED requires.  In my
case, the old fluorescent tube had 4 pins in total (2 at each end), with 3
being connected to active AC (one went via the starter) and the remaining pin
to neutral.  For these replacement LED tubes, this changes to 2 and 2
respectively, with two pins at one end of the tube being wired to active, and
the other end's two pins being connected to neutral.  Adjusting the wiring in
the light fitting is the most complicated step in replacement.


How to
======

This is essentially the same my `first LED replacement post`_, so refer to
that page for greater detail about getting started.

Preparation
-----------

Gather the materials, order the lights, and wait.  Make nice with your
electrician friend and arrange for them to come over and help out when your
lights arrive.

Step by step
------------

Your experience may be different, so adapt the instructions to suit your own
light fittings or LEDs, if ordering different lights.

.. image:: |filename|./images/led-lights/IMG_3658.JPG
    :width: 400px
    :alt: Before, fluorescent tube present


#. Ensure all power is disconnected from the light fitting prior to beginning.
   Isolate the circuit the light is connected to, and use a multimeter to
   double-check the voltage before starting.

#. Unscrew or demount the whole light fitting from the ceiling.  It will make
   working on the fitting much simpler when not working upside down.  Removing
   the tube first before trying to demount the light fitting is the safest
   option.  Disconnect the mains cables from the terminal block in your light
   fitting (or similar).

#. Unscrew and remove all electrical components from the panel.  In this case,
   one would remove the tube, the starter and the electronic ballast.  The
   tube connectors at each end need to remain because the new LED tube will be
   fitted here.

    .. image:: |filename|./images/led-lights/IMG_3661.JPG
        :width: 400px
        :alt: Fluorescent tube removed

   All that should remain in the fitting are the wires running from the
   terminal block to the connectors at both ends.

#. Re-route the wiring in accordance with what the LED tube requires.  Consult
   their documentation for more information.  In my case, this involved
   changing the *active* pin next to the neutral pin from the original
   connector at one end to having both pins be neutral.  Your electrician
   friend should be performing this for you.

#. Fit the reconfigured light fixture back onto the ceiling, reconnecting the
   mains cabling into the original terminal block.

    .. image:: |filename|./images/led-lights/IMG_3664.JPG
        :width: 400px
        :alt: Routing cables and fitting LEDs

#. Fit the new LED tube into the light fitting, and ensure all fittings are
   tight.

#. The end result looks like this:

   .. image:: |filename|./images/led-lights/IMG_3665.JPG
      :width: 400px
      :alt: After - LED board replacement

#. Turn the power back on, and turn on the light switch.

   .. image:: |filename|./images/led-lights/IMG_3666.JPG
      :width: 400px
      :alt: After - light on and installed

#. Repeat for other lights being replaced.


Power comparison
================

======    ============   ===============      =======     ============    =========
Type      Power rating   Brand                Watts       Power Factor    Amps
======    ============   ===============      =======     ============    =========
Fluoro    36W            Compton              42-45       0.76-0.81       0.22-0.23 249.5
LED       18W            Generic Cree         20          1.0             0.08-0.09 250
LED       18W            Generic Cree         17          1.0             0.07-0.08 249.5
======    ============   ===============      =======     ============    =========


As per my `previous post`_, the figures above aren't exactly brimming with
precision.  The power meter I was using monitors amps to 2 decimal places only
(and the reading tends to jump around a bit).  From some of the calculations
I've done, these figures aren't even rounded, they're just truncated.  I've
worked backwards using the voltage, amperage, and power factor to get a truer
indication as to the wattage.  The input power I'm working with is slightly
variable as well, being between 246 and 250V AC.

The comparison between the two lights isn't precisely fair or exact, but it's
close.  The LED replacement is a 180-degree lamp, compared to a 360-degree
lamp in the fluorescent.  Realistically, the fact the light is on the ceiling
facing downwards means the LED is going to excel here, since it is more
direct.

As you can see above, the energy savings are quite significant.  In this case,
the current draw from the LEDs is around one-third that being drawn by the
fluorescent tube, making for a saving of about 66%.  Since the power factor is
higher on the LEDs (being perfect, at 1.0), the effective cost savings for me
(since my power company only charges in Watts) is about 50%.  That's still
significant in anyone's books, and justifies new properties being fitted with
these sorts of lights from the get-go.


Conclusion
==========

Overall, this replacement was extremely successful and completely the
conversion of my house to LEDs, with the exception of the fridge lamp, the
oven lamps, and any other appliances that might be using incandescent or other
types of lighting.  I'll do a retrospective on some of the other lighting I
replaced in my house (halogen downlights, etc) at some point.

As before, there will always be the environmental benefits of not using
mercury lamps and (hopefully) not having to replace the lights ever again.

The power savings are notable, though given the fact I'm not leaving my garage
lights on for many hours at a time, will take a long while before they add up.
The most important cost factor here is in having to replace the tubes, which
given the age of our house, I would have been up for anyway at a near date.

Stay tuned for more of the same as my house becomes more power and energy
efficient!


.. _licence: |filename|pages/licence.rst
.. _1: |filename|2014-07-21-project-green-house-round-leds.rst
.. _2: |filename|2014-10-07-project-green-house-straight-led.rst
.. _first LED replacement post: |filename|2014-07-21-project-green-house-round-leds.rst
.. _previous post: |filename|2014-07-21-project-green-house-round-leds.rst
.. _Lighting Research Center: http://www.lrc.rpi.edu/programs/nlpip/lightingAnswers/lat5/abstract.asp
