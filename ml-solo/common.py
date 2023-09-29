from os.path import expanduser

DATASET_DIR = "~/Ai/Ia-Datasets/DATAS"


def get_dataset_dir(dir):
    return expanduser(f"{DATASET_DIR}/{dir}")


def test_conclude(test_result, reverse=False):
    """
    test_result : result of a test
    reverse : if True, the test is reversed. It's for example for a normality test or a homogeneity test.
    """
    print(test_result)
    print(
        f"pvalue is showing valid study : {test_result.pvalue < 0.05 if  not reverse else test_result.pvalue > 0.05}."
    )
    if hasattr(test_result, "dof"):
        print(f"Le degre de liberté : {test_result.dof}")
