package com.manoj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ExecPythonProgramFromJava {

	public static void main(String[] args) throws IOException {

		ProcessBuilder pb = new ProcessBuilder("python", "helloworld.py");
		Process p = pb.start();

		BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
		System.out.println(in.readLine());

	}

}
