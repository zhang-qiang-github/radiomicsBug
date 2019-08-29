from radiomics import featureextractor
extractor = featureextractor.RadiomicsFeatureExtractor()
result = extractor.execute(imageFilepath='tempFolder\image.nrrd', maskFilepath='tempFolder\mask.nrrd')
keys = list(result.keys())

for index, key in enumerate(keys):
    print(index, key)