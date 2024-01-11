setup_fvm:
	##########################
	# add basic dependencies #
	##########################
	fvm flutter pub add flutter_bloc
	fvm flutter pub add intl:0.18.1 # to be adjusted later on
	fvm flutter pub add auto_route
	fvm flutter pub add flutter_localizations --sdk=flutter

	########################
	# add dev dependencies #
	########################

	fvm flutter pub add -d auto_route_generator
	fvm flutter pub add -d build_runner
	fvm flutter pub add -d json_serializable

	##############################
	# get all added dependencies #
	############################## 
	fvm flutter pub get

	###########################
	# execute code generation #
	########################### 
	fvm flutter gen-l10n
	fvm flutter packages pub run build_runner build --delete-conflicting-outputs