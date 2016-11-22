import groovy.json.JsonSlurper

//**********************************************************************
// Define constants
//**********************************************************************
def DAYS2KEEP = 30
def NUM2KEEP = 100

//**********************************************************************
// Define parameters with default settings
//**********************************************************************
def ci_job_name_root = 'run-single-trial'
def fish = "Harlene"
def thatpistimulus = "0"
def pistimulus = "0.png"
def correctside = "B"
def day = "1"
def session = "1"
def feedside = "both"
def sex = "female"
def proportion = "0"
def species = "gambusia"
def fishstandardlength = "TBD"
def round = "7"
def camera = "FALSE"
def node = "master"
def cam_node = "master"

//**********************************************************************
//Read in json files
//**********************************************************************
println("Current dir: " + System.getProperty("user.dir") + "\n")

def slurper = new JsonSlurper()

//Read in H1 schedule
File f = new File('/var/lib/jenkins/workspace/dsl_seed_job/H1.json')
def jsonText = f.getText()
jsonH1 = slurper.parseText(jsonText)
println("H1 schedule: \n" + jsonH1 + "\n")

//Read in H2 schedule
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/H2.json')
jsonText = f.getText()
jsonH2 = slurper.parseText(jsonText)
println("H2 schedule: \n" + jsonH2 + "\n")

//Read in H3 schedule
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/H3.json')
jsonText = f.getText()
jsonH3 = slurper.parseText(jsonText)
println("H3 schedule: \n" + jsonH3 + "\n")

//Read in L1 schedule
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/L1.json')
jsonText = f.getText()
jsonL1 = slurper.parseText(jsonText)
println("L1 schedule: \n" + jsonL1 + "\n")

//Read in L2 schedule
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/L2.json')
jsonText = f.getText()
jsonL2 = slurper.parseText(jsonText)
println("L2 schedule: \n" + jsonL2 + "\n")

//Read in L3 schedule
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/L3.json')
jsonText = f.getText()
jsonL3 = slurper.parseText(jsonText)
println("L3 schedule: \n" + jsonL3 + "\n")

//Read in Fish specific parameters
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/fish.json')
jsonText = f.getText()
jsonFish = slurper.parseText(jsonText)
println("Fish: \n" + jsonFish + "\n")

//Read in top level parameters
f = new File('/var/lib/jenkins/workspace/dsl_seed_job/top.json')
jsonText = f.getText()
jsonTop = slurper.parseText(jsonText)
println("Top: \n" + jsonTop + "\n")
round = jsonTop."round"
println("round=" + round)
def startDate = jsonTop."startDate"
println("startDate=" + startDate)
String h1_fish = jsonTop."mapping"."H1"
println("h1_fish=" + h1_fish)
String h2_fish = jsonTop."mapping"."H2"
println("h2_fish=" + h2_fish)
String h3_fish = jsonTop."mapping"."H3"
println("h3_fish=" + h3_fish)
String l1_fish = jsonTop."mapping"."L1"
println("l1_fish=" + l1_fish)
String l2_fish = jsonTop."mapping"."L2"
println("l2_fish=" + l2_fish)
String l3_fish = jsonTop."mapping"."L3"
println("l3_fish=" + l3_fish)

println("\n*****************H1 Schedule *****************")
if (h1_fish != "null") {
	fish = h1_fish
	fishstandardlength = jsonFish.(fish.toString())."fishstandardlength"
	species = jsonFish.(fish.toString())."species"
	sex = jsonFish.(fish.toString())."sex"
	node = jsonFish.(fish.toString())."node"
	cam_node = jsonFish.(fish.toString())."cam_node"
	println("fish=" + fish)
	println("sex=" + sex)
	println("species=" + species)
	println("fishstandardlength=" + fishstandardlength)
	println("node=" + node)
	println("cam_node=" + cam_node)
	println("\n")
	//Loop over each trial and create a CI job
	for (item in jsonH1) {
		println("\n#######################")
		println("Sub-trial #" + item.key)
		println("#######################")
		day = jsonH1.(item.key)."day"
		time = jsonH1.(item.key)."time"
		thatpistimulus = jsonH1.(item.key)."thatpistimulus"
		pistimulus = jsonH1.(item.key)."pistimulus"
		correctside = jsonH1.(item.key)."correctside"
		session = jsonH1.(item.key)."session"
		feedside = jsonH1.(item.key)."feedside"
		proportion = jsonH1.(item.key)."proportion"
		feed = jsonH1.(item.key)."feed"
		camera = jsonH1.(item.key)."camera"
		println("day=" + day)
		println("time=" + time)
		println("thatpistimulus=" + thatpistimulus)
		println("pistimulus=" + pistimulus)
		println("correctside=" + correctside)
		println("session=" + session)
		println("feedside=" + feedside)
		println("proportion=" + proportion)
		println("feed=" + feed)
		println("camera=" + camera)
		
		//Build up job name, fish + sub-trial #
		ci_job_name = ci_job_name_root + "_" + fish + "_" + item.key
		
		//Decide between node with or without camera
		if(camera == "TRUE") {
			node = cam_node
		}
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, fish, thatpistimulus, pistimulus, \
		    correctside, day, session, feedside, sex, proportion, species, \
		    fishstandardlength, round, camera, node, startDate)
	}
}
println("*****************End of H1 Schedule *****************")

println("\n*****************H2 Schedule *****************")
if (h2_fish != "null") {
	fish = h2_fish
	fishstandardlength = jsonFish.(fish.toString())."fishstandardlength"
	species = jsonFish.(fish.toString())."species"
	sex = jsonFish.(fish.toString())."sex"
	node = jsonFish.(fish.toString())."node"
	cam_node = jsonFish.(fish.toString())."cam_node"
	println("fish=" + fish)
	println("sex=" + sex)
	println("species=" + species)
	println("fishstandardlength=" + fishstandardlength)
	println("node=" + node)
	println("cam_node=" + cam_node)
	println("\n")
	//Loop over each trial and create a CI job
	for (item in jsonH2) {
		println("\n#######################")
		println("Sub-trial #" + item.key)
		println("#######################")
		day = jsonH2.(item.key)."day"
		time = jsonH2.(item.key)."time"
		thatpistimulus = jsonH2.(item.key)."thatpistimulus"
		pistimulus = jsonH2.(item.key)."pistimulus"
		correctside = jsonH2.(item.key)."correctside"
		session = jsonH2.(item.key)."session"
		feedside = jsonH2.(item.key)."feedside"
		proportion = jsonH2.(item.key)."proportion"
		feed = jsonH2.(item.key)."feed"
		camera = jsonH2.(item.key)."camera"
		println("day=" + day)
		println("time=" + time)
		println("thatpistimulus=" + thatpistimulus)
		println("pistimulus=" + pistimulus)
		println("correctside=" + correctside)
		println("session=" + session)
		println("feedside=" + feedside)
		println("proportion=" + proportion)
		println("feed=" + feed)
		println("camera=" + camera)
		
		//Build up job name, fish + sub-trial #
		ci_job_name = ci_job_name_root + "_" + fish + "_" + item.key
		
		//Decide between node with or without camera
		if(camera == "TRUE") {
			node = cam_node
		}
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, fish, thatpistimulus, pistimulus, \
		    correctside, day, session, feedside, sex, proportion, species, \
		    fishstandardlength, round, camera, node, startDate)
	}
}
println("*****************End of H2 Schedule *****************")

println("\n*****************H3 Schedule *****************")
if (h3_fish != null) {
	fish = h3_fish
	fishstandardlength = jsonFish.(fish.toString())."fishstandardlength"
	species = jsonFish.(fish.toString())."species"
	sex = jsonFish.(fish.toString())."sex"
	node = jsonFish.(fish.toString())."node"
	cam_node = jsonFish.(fish.toString())."cam_node"
	println("fish=" + fish)
	println("sex=" + sex)
	println("species=" + species)
	println("fishstandardlength=" + fishstandardlength)
	println("node=" + node)
	println("cam_node=" + cam_node)
	println("\n")
	//Loop over each trial and create a CI job
	for (item in jsonH3) {
		println("\n#######################")
		println("Sub-trial #" + item.key)
		println("#######################")
		day = jsonH3.(item.key)."day"
		time = jsonH3.(item.key)."time"
		thatpistimulus = jsonH3.(item.key)."thatpistimulus"
		pistimulus = jsonH3.(item.key)."pistimulus"
		correctside = jsonH3.(item.key)."correctside"
		session = jsonH3.(item.key)."session"
		feedside = jsonH3.(item.key)."feedside"
		proportion = jsonH3.(item.key)."proportion"
		feed = jsonH3.(item.key)."feed"
		camera = jsonH3.(item.key)."camera"
		println("day=" + day)
		println("time=" + time)
		println("thatpistimulus=" + thatpistimulus)
		println("pistimulus=" + pistimulus)
		println("correctside=" + correctside)
		println("session=" + session)
		println("feedside=" + feedside)
		println("proportion=" + proportion)
		println("feed=" + feed)
		println("camera=" + camera)
		
		//Build up job name, fish + sub-trial #
		ci_job_name = ci_job_name_root + "_" + fish + "_" + item.key
		
		//Decide between node with or without camera
		if(camera == "TRUE") {
			node = cam_node
		}
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, fish, thatpistimulus, pistimulus, \
		    correctside, day, session, feedside, sex, proportion, species, \
		    fishstandardlength, round, camera, node, startDate)
	}
}
println("*****************End of H3 Schedule *****************")

println("\n*****************L1 Schedule *****************")
if (l1_fish != null) {
	fish = l1_fish
	fishstandardlength = jsonFish.(fish.toString())."fishstandardlength"
	species = jsonFish.(fish.toString())."species"
	sex = jsonFish.(fish.toString())."sex"
	node = jsonFish.(fish.toString())."node"
	cam_node = jsonFish.(fish.toString())."cam_node"
	println("fish=" + fish)
	println("sex=" + sex)
	println("species=" + species)
	println("fishstandardlength=" + fishstandardlength)
	println("node=" + node)
	println("cam_node=" + cam_node)
	println("\n")
	//Loop over each trial and create a CI job
	for (item in jsonL1) {
		println("\n#######################")
		println("Sub-trial #" + item.key)
		println("#######################")
		day = jsonL1.(item.key)."day"
		time = jsonL1.(item.key)."time"
		thatpistimulus = jsonL1.(item.key)."thatpistimulus"
		pistimulus = jsonL1.(item.key)."pistimulus"
		correctside = jsonL1.(item.key)."correctside"
		session = jsonL1.(item.key)."session"
		feedside = jsonL1.(item.key)."feedside"
		proportion = jsonL1.(item.key)."proportion"
		feed = jsonL1.(item.key)."feed"
		camera = jsonL1.(item.key)."camera"
		println("day=" + day)
		println("time=" + time)
		println("thatpistimulus=" + thatpistimulus)
		println("pistimulus=" + pistimulus)
		println("correctside=" + correctside)
		println("session=" + session)
		println("feedside=" + feedside)
		println("proportion=" + proportion)
		println("feed=" + feed)
		println("camera=" + camera)
		
		//Build up job name, fish + sub-trial #
		ci_job_name = ci_job_name_root + "_" + fish + "_" + item.key
		
		//Decide between node with or without camera
		if(camera == "TRUE") {
			node = cam_node
		}
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, fish, thatpistimulus, pistimulus, \
		    correctside, day, session, feedside, sex, proportion, species, \
		    fishstandardlength, round, camera, node, startDate)
	}
}
println("*****************End of L1 Schedule *****************")

println("\n*****************L2 Schedule *****************")
if (l2_fish != null) {
	fish = l2_fish
	fishstandardlength = jsonFish.(fish.toString())."fishstandardlength"
	species = jsonFish.(fish.toString())."species"
	sex = jsonFish.(fish.toString())."sex"
	node = jsonFish.(fish.toString())."node"
	cam_node = jsonFish.(fish.toString())."cam_node"
	println("fish=" + fish)
	println("sex=" + sex)
	println("species=" + species)
	println("fishstandardlength=" + fishstandardlength)
	println("node=" + node)
	println("cam_node=" + cam_node)
	println("\n")
	//Loop over each trial and create a CI job
	for (item in jsonL2) {
		println("\n#######################")
		println("Sub-trial #" + item.key)
		println("#######################")
		day = jsonL2.(item.key)."day"
		time = jsonL2.(item.key)."time"
		thatpistimulus = jsonL2.(item.key)."thatpistimulus"
		pistimulus = jsonL2.(item.key)."pistimulus"
		correctside = jsonL2.(item.key)."correctside"
		session = jsonL2.(item.key)."session"
		feedside = jsonL2.(item.key)."feedside"
		proportion = jsonL2.(item.key)."proportion"
		feed = jsonL2.(item.key)."feed"
		camera = jsonL2.(item.key)."camera"
		println("day=" + day)
		println("time=" + time)
		println("thatpistimulus=" + thatpistimulus)
		println("pistimulus=" + pistimulus)
		println("correctside=" + correctside)
		println("session=" + session)
		println("feedside=" + feedside)
		println("proportion=" + proportion)
		println("feed=" + feed)
		println("camera=" + camera)
		
		//Build up job name, fish + sub-trial #
		ci_job_name = ci_job_name_root + "_" + fish + "_" + item.key
		
		//Decide between node with or without camera
		if(camera == "TRUE") {
			node = cam_node
		}
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, fish, thatpistimulus, pistimulus, \
		    correctside, day, session, feedside, sex, proportion, species, \
		    fishstandardlength, round, camera, node, startDate)
	}
}
println("*****************End of L2 Schedule *****************")

println("\n*****************L3 Schedule *****************")
if (l3_fish != null) {
	fish = l3_fish
	fishstandardlength = jsonFish.(fish.toString())."fishstandardlength"
	species = jsonFish.(fish.toString())."species"
	sex = jsonFish.(fish.toString())."sex"
	node = jsonFish.(fish.toString())."node"
	cam_node = jsonFish.(fish.toString())."cam_node"
	println("fish=" + fish)
	println("sex=" + sex)
	println("species=" + species)
	println("fishstandardlength=" + fishstandardlength)
	println("node=" + node)
	println("cam_node=" + cam_node)
	println("\n")
	//Loop over each trial and create a CI job
	for (item in jsonL3) {
		println("\n#######################")
		println("Sub-trial #" + item.key)
		println("#######################")
		day = jsonL3.(item.key)."day"
		time = jsonL3.(item.key)."time"
		thatpistimulus = jsonL3.(item.key)."thatpistimulus"
		pistimulus = jsonL3.(item.key)."pistimulus"
		correctside = jsonL3.(item.key)."correctside"
		session = jsonL3.(item.key)."session"
		feedside = jsonL3.(item.key)."feedside"
		proportion = jsonL3.(item.key)."proportion"
		feed = jsonL3.(item.key)."feed"
		camera = jsonL3.(item.key)."camera"
		println("day=" + day)
		println("time=" + time)
		println("thatpistimulus=" + thatpistimulus)
		println("pistimulus=" + pistimulus)
		println("correctside=" + correctside)
		println("session=" + session)
		println("feedside=" + feedside)
		println("proportion=" + proportion)
		println("feed=" + feed)
		println("camera=" + camera)
		
		//Build up job name, fish + sub-trial #
		ci_job_name = ci_job_name_root + "_" + fish + "_" + item.key
		
		//Decide between node with or without camera
		if(camera == "TRUE") {
			node = cam_node
		}
		
		//Create CI job
		createCiJob(ci_job_name, DAYS2KEEP, NUM2KEEP, fish, thatpistimulus, pistimulus, \
		    correctside, day, session, feedside, sex, proportion, species, \
		    fishstandardlength, round, camera, node, startDate)
	}
}
println("*****************End of L3 Schedule *****************")

//**********************************************************************
// Function creates CI job with specified parameters
//**********************************************************************
def createCiJob(def ci_job_name, def DAYS2KEEP, def NUM2KEEP, def fish, \
                def thatpistimulus, def pistimulus, def correctside, \
                def day, def session, def feedside, def sex, def proportion, \
                def species, def fishstandardlength, def round, def camera, \
                def node, def startDate) {
	job(ci_job_name){
	  logRotator {
		daysToKeep(DAYS2KEEP)
		numToKeep(NUM2KEEP)
	  }
	  
	  //parameters {
	  //  stringParam("fish", fish)
	  //}
	  
	  //Container job runs on master, sub-job will be executed on NODE specified parameter
	  label("master")
	  
	  // TODO: pull scripts from github, will also house json files there
	  //		what about the dsl file?
	  //scm{
	  //
	  //}
	  
	  //Spec syntax, similar to cron
	  //MINUTE 	Minutes within the hour (0–59)
	  //HOUR 	The hour of the day (0–23)
	  //DOM 	The day of the month (1–31)
	  //MONTH 	The month (1–12)
	  //DOW 	The day of the week (0–7) where 0 and 7 are Sunday.
	  def (HOUR, MINUTE) = time.tokenize( ':' )
	  //println("HOUR=" + HOUR)
	  //println("MINUTE=" + MINUTE)
	  def (MONTH, DOM) = startDate.tokenize( '/' )
	  //println("MONTH=" + MONTH)
	  //println("DOM=" + DOM)
	  
	  //This mapping will be okay until Feb 2020
	  def days_in_month_map  = new HashMap<String,Integer>()
	  days_in_month_map.put("1", 31)
	  days_in_month_map.put("2", 28)
	  days_in_month_map.put("3", 31)
	  days_in_month_map.put("4", 30)
	  days_in_month_map.put("5", 31)
	  days_in_month_map.put("6", 30)
	  days_in_month_map.put("7", 31)
	  days_in_month_map.put("8", 31)
	  days_in_month_map.put("9", 30)
	  days_in_month_map.put("10", 31)
	  days_in_month_map.put("11", 30)
	  days_in_month_map.put("12", 31)

	  //Adjust day/month based on day parameter
	  if(((day.toInteger()-1) + DOM.toInteger()) > days_in_month_map.(MONTH.toString())) {
		if(MONTH != "12") {
			MONTH =(MONTH.toInteger() + 1).toString()
		} else {
			MONTH = "1"
		}
		DOM = (((day.toInteger()-1) + DOM.toInteger()) - days_in_month_map.(MONTH.toString())).toString()
	  } else {
		DOM = (DOM.toInteger() + day.toInteger() - 1).toString()
	  }	  
	  //println("adjMONTH=" + MONTH)
	  //println("adjDOM=" + DOM)
	  
	  //Trigger build based on startDate, date, and time parameters
	  println("Triggering build on MONTH=" + MONTH + ", DAY=" + DOM + ", HOUR=" + HOUR + ", MINUTE=" + MINUTE)
	  triggers {
				timerTrigger{
							 spec(MINUTE + " " + HOUR + " " + DOM + " " + MONTH + " *")
				}
	  }
	  
	  //wrappers {
	  //  preBuildCleanUp()
	  //}
	  
	  steps {
		//shell('echo "Hello World!"')		
		triggerBuilder {
		  configs {
			  blockableBuildTriggerConfig {
				  projects("RunSingleTrial")
				  block {
					  buildStepFailureThreshold("FAILURE")
					  unstableThreshold("UNSTABLE")
					  failureThreshold("FAILURE")
				  } //block
				  configFactories {}
				  configs {
					  predefinedBuildParameters {
						properties("fish=" + fish + 
								   "\nthatpistimulus=" + thatpistimulus +
								   "\npistimulus=" + pistimulus +
								   "\ncorrectside=" + correctside + 
								   "\nday=" + day +
								   "\nsession=" + session +
								   "\nfeedside=" + feedside +
								   "\nsex=" + sex +
								   "\nproportion=" + proportion +
								   "\nspecies=" + species +
								   "\nfishstandardlength=" + fishstandardlength +
								   "\nround=" + round +
								   "\ncamera=" + camera +
								   "\nNODE=" + node)
					  }
				  } //configs
			  } //blockableBuildTriggerConfig
		  } //configs
		}  //triggerBuilder
	  } //steps
	  //publishers {
	  //	archiveArtifacts('*.*')
	  //}
	} //job
} //createCiJob
