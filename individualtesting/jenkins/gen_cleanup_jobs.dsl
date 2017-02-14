import groovy.json.JsonSlurper

//**********************************************************************
// Define constants
//**********************************************************************
def DAYS2KEEP = 30
def NUM2KEEP = 100

//**********************************************************************
// Define parameters with default settings
//**********************************************************************
def ci_job_name_root = 'cleanup-job'

//**********************************************************************
//Read in json file
//**********************************************************************
println("Current dir: " + System.getProperty("user.dir") + "\n")

def slurper = new JsonSlurper()

File f = new File('/var/lib/jenkins/workspace/cleanup-dsl-seed-job/trashcan.json')
def jsonText = f.getText()
jsonTc = slurper.parseText(jsonText)
println("Trashcan: \n" + jsonTc + "\n")

//Loop through schedules
nodes = ["node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12"]

for (node in nodes) {
	if (node in jsonTc) {
		println("\n#######################")
		println("Cleaning up " + jsonTc.node)
		println("#######################")
		
		//Build up job name
		ci_job_name = ci_job_name_root + "_" + jsonTc.node
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, jsonTc.node)
		
		queue(ci_job_name)
		
		println("*******************************************************************")
	}
}

//**********************************************************************
// Function creates CI job with specified parameters
//**********************************************************************
def createCiJob(def ci_job_name, def DAYS2KEEP, def NUM2KEEP, def this_node) {
	job(ci_job_name){
	  logRotator {
		daysToKeep(DAYS2KEEP)
		numToKeep(NUM2KEEP)
	  }
	  
	  //Container job runs on master, sub-job will be executed on NODE specified parameter
	  label(this_node)
	  
	  // run shell that deletes workspace
	  steps {			
		shell ( "cd ..; rm -rf *" )
	  } //steps
	} //job
} //createCiJob
