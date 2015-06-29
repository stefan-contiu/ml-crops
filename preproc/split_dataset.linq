<Query Kind="Program" />

int PERCENT_TEST_SET = 10;  // define percentage of test set from whole data set

string datasetFileName = @"d:\CODE\ml-crops\preproc\dataset_v2.csv";

string trainFeaturesFileName = @"d:\CODE\ml-crops\preproc\features_train.csv";
string trainClassesFileName = @"d:\CODE\ml-crops\preproc\classes_train.csv";

string testFeaturesFileName = @"d:\CODE\ml-crops\preproc\features_test.csv";
string testClassesFileName = @"d:\CODE\ml-crops\preproc\classes_test.csv";

void Main()
{
	int totalLines = 0; 
	StreamReader datasetReader = new StreamReader(datasetFileName);
	while(!datasetReader.EndOfStream)
	{
		datasetReader.ReadLine();
		totalLines++;
	}
	datasetReader.Close();
	Console.WriteLine("Total Lines in input set : " + totalLines);
	
	int test_item_count = (PERCENT_TEST_SET * totalLines) / 100;
	Console.WriteLine("Generating " + test_item_count + " random indexes ... ");
	HashSet<int> indexes = new HashSet<int>();	
	Random rand = new Random();
	for(int test_item_index = 0; test_item_index < test_item_count; test_item_index++)
	{
		int i = rand.Next() % totalLines;
		while(indexes.Contains(i)) i = rand.Next() % totalLines;
	
		indexes.Add(i);
	}
	Console.WriteLine("Finished generating " + indexes.Count() + " indexes.");
	
	
	// split the big dataset according to the random indexes
	StreamWriter features_train = new StreamWriter(trainFeaturesFileName);
	StreamWriter classes_train = new StreamWriter(trainClassesFileName);
	StreamWriter features_test = new StreamWriter(testFeaturesFileName);
	StreamWriter classes_test = new StreamWriter(testClassesFileName);
	
	datasetReader = new StreamReader(datasetFileName);
	datasetReader.ReadLine(); // skip first mocked line
	int lineIndex = 1;
	while(!datasetReader.EndOfStream)
	{
		// read data set line
		string line = datasetReader.ReadLine();
		// extract features and class
		string s_features = line.Substring(0, line.LastIndexOf(','));
		string s_class = line.Substring(line.LastIndexOf(',') + 1);
		if (indexes.Contains(lineIndex))
		{
			// goes to the test set
			features_test.WriteLine(s_features);
			classes_test.WriteLine(s_class);						
		}
		else
		{
			// goes to the train set
			features_train.WriteLine(s_features);
			classes_train.WriteLine(s_class);
		}
		
		lineIndex++;
	}
	datasetReader.Close();

	features_train.Close();
	classes_train.Close();
	features_test.Close();
	classes_test.Close();
	
	Console.WriteLine("Train and test sets generated succesfully !");
}
// Define other methods and classes here