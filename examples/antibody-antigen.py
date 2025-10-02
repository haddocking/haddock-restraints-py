# ===========================================================================#
#
# EXAMPLE: Antibody-Antigen interaction
#
# This example shows how to define the interaction between an antibody
#  and an antigen using the haddock-restraints library.
#
# This example is based on the following tutorial:
#  <https://www.bonvinlab.org/education/HADDOCK3/HADDOCK3-antibody-antigen/>
#
# Here we demonstrate how to use the `haddock-restraints` library to
#  generate the restraints to be used in the docking.
#
# ===========================================================================#

from haddock_restraints import Interactor, Air


def main():

    # Define active residues of the EPITOPE
    epitope_active_residues = [
        72,
        73,
        74,
        75,
        81,
        83,
        84,
        89,
        90,
        92,
        94,
        96,
        97,
        98,
        115,
        116,
        117,
    ]

    # Define active residues of the PARATOPE
    paratope_active_residues = [
        1,
        32,
        33,
        34,
        35,
        52,
        54,
        55,
        56,
        100,
        101,
        102,
        103,
        104,
        105,
        106,
        151,
        152,
        169,
        170,
        173,
        211,
        212,
        213,
        214,
        216,
    ]

    # Define the Epitope and Paratope interactors
    epitope = Interactor(id=1, chain="H", active=epitope_active_residues, passive=[])
    paratope = Interactor(id=2, chain="L", active=paratope_active_residues, passive=[])

    # Add a reference PDB structure to the epitope
    epitope.set_pdb("data/4I1B_clean.pdb")
    # Define the passive residues based on the active ones
    epitope.set_passive_from_active()

    # Define the relationship between the interactors
    #  here they interact with each other
    epitope.set_target(2)
    paratope.set_target(1)

    # Initialize the AIR object with the interactors
    air = Air(interactors=[epitope, paratope])

    # Create the TBL formatted output
    tbl = air.gen_tbl()

    # Print the TBL formatted output
    print(tbl)

    # Alternatively, save the TBL formatted output to a file
    # with open("antibody-antigen.tbl", "w") as f:
    #     f.write(tbl)


if __name__ == "__main__":
    main()
