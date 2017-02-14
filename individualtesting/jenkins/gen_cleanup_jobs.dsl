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

//Loop through schedules
nodes = ["mercury", "venus"]
for (node in nodes) {
	println("\n#######################")
	println("Cleaning up " + node)
	println("#######################")
	
	//Build up job name
	ci_job_name = ci_job_name_root + "_" + node
	
	//Create CI job
	createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, node)
	
	queue(ci_job_name)
	
	println("*******************************************************************")
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
