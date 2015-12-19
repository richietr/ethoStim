# ethoStim
These scripts control stimuli being used to measure social and non-social learning and fear response in poecillid fishes under pharmaceutical manipulations of the NMDA receptor pathway.

pooky.py controls the stimulus and data collection for a numerosity (learning) assay, for two fish at a time in adjoining tanks setup in this way:

        The Left tank's stimulus orientation determine the stimID
        The Right tank's stimulus are dependent and inverse
        SO:

        Left tank        Right tank
        |            |   |            |
        |            |   |            |
        |High     Low|___|Low     High|
        ______________   ______________

        would result in a stimID of 'int(High)_int(Low)'

                Left tank        Right tank
                |            |   |            |
                |            |   |            |
                |Low     High|___|High     Low|
                ______________   ______________

                would result in a stimID of 'int(Low)_int(High)'

        The individuals in each tank determine which side the reward condition
        will be presented (but these will always be the same side for both
        tanks in any given trial as long as a 'High' and 'Low' individual are
        always paired

        e.g.:

        Left tank        Right tank
        HIGH FISH        LOW FISH
        fed side (Left):
          |                |
          V                V
        |            |   |            |
        |            |   |            |
        |High     Low|___|Low     High|
        ______________   ______________

                Left tank        Right tank
                LOW FISH         HIGH FISH
                fed side (Right):
                           |                |
                           V                V
                |            |   |            |
                |            |   |            |
                |High     Low|___|Low     High|
                ______________   ______________

        the inverse is also possible as the 'High' and 'Low' sides are randomized


usage exampe: python pooky.py --day [0] --session [1] --leftFish [Liljohn] --rightFish [Ladygaga] --highStim [12] --lowStim [6] --fedSide [both] --species [sailfin] --round [3] --rightfishstandardlength [240] --leftfishstandardlength [220] --rightfishsex [F] --leftfishsex [M]
(ommiting brackets)

I find that it is best to generate these file names with a script or spreadsheet instead of typing them in.


Processing and analysis scripts can be found at RobertIan/LearningFearandMateChoice
