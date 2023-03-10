#version 330 core
//so we have verteces as 3 component vector in position
layout (location=0) in vec3 in_position;


void main(){
    //passing it to the gl for further rasterization process
    gl_Position = vec4(in_position, 1.0);
}