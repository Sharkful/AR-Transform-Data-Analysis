# Open the file
dataFile = open("data.bin")

# Variables
# Time in seconds since the start of the application
startTime = read(dataFile, Float32)
# Time in seconds after the set deltaTime (0.5s rn)
deltaTime_offsets = Vector{Float32}(undef,0)
# Tuples of 3D position at each timestep of the controller
controller_positions = Vector{Tuple{Float32,Float32,Float32}}(undef,0)
# Tuples of the 4D rotation at each timestep of the controller
controller_rotations = Vector{Tuple{Float32,Float32,Float32,Float32}}(undef,0)
# Tuples of 3D position at each timestep of the headset
headset_positions = Vector{Tuple{Float32,Float32,Float32}}(undef,0)
# Tuples of the 4D rotation at each timestep of the headset
headset_rotations = Vector{Tuple{Float32,Float32,Float32,Float32}}(undef,0)

# Read to the end of the file
while !eof(dataFile)
    # Read in the first offset value for the timestamp
    push!(deltaTime_offsets, read(dataFile, Float32))
    # Read in 12 bytes of data, reinterperet as 3 element Float 32 array, convert to tuple
    push!(controller_positions,
          Tuple(x for x in 
                reinterpret(Float32,
                            read(dataFile, 4*3))))
    # Ditto, but 16 bytes, 4 element array
    push!(controller_rotations,
          Tuple(x for x in 
                reinterpret(Float32,
                            read(dataFile, 4*4))))
    push!(headset_positions,
          Tuple(x for x in 
                reinterpret(Float32,
                            read(dataFile, 4*3))))
    push!(headset_rotations,
          Tuple(x for x in 
                reinterpret(Float32,
                            read(dataFile, 4*4))))
end

# Test print out
println("Successfully read all the data")
println(controller_positions)
