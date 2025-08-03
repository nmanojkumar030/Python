#!/usr/bin/env python3
"""
Script to rename Python files in the python_concepts folder with more meaningful names.
This script will rename files based on the suggested naming conventions.
"""

import os
import shutil
from pathlib import Path

# Mapping of old names to new names
file_rename_mapping = {
    # Data Structure & Collection Examples
    'Accessing_Lists.py': 'list_access_methods.py',
    'Creating_Lists.py': 'list_creation_examples.py',
    'Searching_Lists.py': 'list_search_operations.py',
    'Slicing_Lists.py': 'list_slicing_demo.py',
    'Negative_Indexing.py': 'negative_indexing_demo.py',
    'list_examples.py': 'list_basic_operations.py',
    'list_copy_examples.py': 'list_copy_methods.py',
    'list_slicing_examples.py': 'list_slicing_advanced.py',
    'list_comprehension_examples.py': 'list_comprehension_demo.py',
    'list_operations.py': 'list_advanced_operations.py',
    'dictionary_basics.py': 'dictionary_fundamentals.py',
    'dictionary_advanced.py': 'dictionary_advanced_operations.py',
    'tuple_operations.py': 'tuple_basic_operations.py',
    
    # String Operations
    'string_operations_01.py': 'string_basic_operations.py',
    'string_iteration_01.py': 'string_iteration_demo.py',
    'string_formatting_01.py': 'string_formatting_basic.py',
    'string_formatting_02.py': 'string_formatting_advanced.py',
    'string_tokenization_01.py': 'string_tokenization_demo.py',
    'string_processor.py': 'string_processing_utilities.py',
    'string_transformer.py': 'string_transformation_basic.py',
    'string_transformer_v2.py': 'string_transformation_advanced.py',
    
    # Functional Programming
    'lambda.py': 'lambda_function_basics.py',
    'lambda_basics.py': 'lambda_function_examples.py',
    'lambda_advanced.py': 'lambda_advanced_usage.py',
    'lambda_with_filters.py': 'lambda_with_filter_function.py',
    'lambda_with_reduce.py': 'lambda_with_reduce_function.py',
    'map.py': 'map_function_examples.py',
    'Filter.py': 'filter_function_examples.py',
    'functional_programming_2.py': 'functional_programming_concepts.py',
    'functional_programming_3.py': 'functional_programming_advanced.py',
    
    # Object-Oriented Programming
    'object_oriented_basics.py': 'oop_fundamentals.py',
    'oop_basics.py': 'oop_class_basics.py',
    'oop_encapsulation.py': 'oop_encapsulation_demo.py',
    'oop_inheritance.py': 'oop_inheritance_demo.py',
    'oop_polymorphism.py': 'oop_polymorphism_demo.py',
    'employee_class.py': 'employee_class_example.py',
    'class_members_demo.py': 'class_members_examples.py',
    'method_resolution_demo.py': 'method_resolution_order.py',
    'multiple_inheritance_demo.py': 'multiple_inheritance_example.py',
    'pass_by_reference_demo.py': 'pass_by_reference_example.py',
    
    # File & System Operations
    'file_operations.py': 'file_io_operations.py',
    'file_archiver.py': 'file_archiving_utility.py',
    'directory_listing.py': 'directory_traversal_demo.py',
    'directory_to_json.py': 'directory_to_json_converter.py',
    'os_server_demo.py': 'os_server_example.py',
    'psoswalk.py': 'directory_walk_utility.py',
    'psoswalk2.py': 'directory_walk_advanced.py',
    'psoswalk3.py': 'directory_walk_filtered.py',
    
    # Regular Expressions
    'psdemregex1.py': 'regex_greedy_vs_non_greedy.py',
    'psdemregex2.py': 'regex_pattern_matching.py',
    'psdemregex3.py': 'regex_character_classes.py',
    'psdemregex4.py': 'regex_quantifiers.py',
    'psdemregex5.py': 'regex_groups_capturing.py',
    'psdemregex6.py': 'regex_substitution.py',
    
    # CSV Processing
    'csv_parser_basic.py': 'csv_reader_basic.py',
    'csv_parser_advanced.py': 'csv_reader_advanced.py',
    'csv_parser_with_pandas.py': 'csv_pandas_processing.py',
    'csv_parser_with_writer.py': 'csv_writer_examples.py',
    
    # Generators & Iterators
    'generator_basics.py': 'generator_fundamentals.py',
    'generator_examples_1.py': 'generator_basic_examples.py',
    'generator_examples_2.py': 'generator_advanced_examples.py',
    'generator_expressions.py': 'generator_expressions_demo.py',
    'generator_functions.py': 'generator_function_examples.py',
    'iterator_examples.py': 'iterator_basic_examples.py',
    'psparallelitr.py': 'parallel_iterator_demo.py',
    
    # Vowel Counter Examples
    'vowel_counter_simple.py': 'vowel_counter_basic.py',
    'vowel_counter_function.py': 'vowel_counter_with_function.py',
    'vowel_counter_dict.py': 'vowel_counter_with_dict.py',
    'vowel_counter_set.py': 'vowel_counter_with_set.py',
    'vowel_counter_comprehension.py': 'vowel_counter_with_comprehension.py',
    'vowel_counter_advanced.py': 'vowel_counter_advanced_approach.py',
    'vowel_search.py': 'vowel_search_utility.py',
    'vowel_search_module.py': 'vowel_search_module_example.py',
    
    # Utility & Demo Programs
    'psdemoint.py': 'integer_operations_demo.py',
    'psdemoio.py': 'input_output_demo.py',
    'psdemoloop.py': 'loop_control_demo.py',
    'psvarargument.py': 'variable_arguments_demo.py',
    'psperson.py': 'person_class_example.py',
    'pspf1.py': 'pickle_file_example.py',
    'psreadjson.py': 'json_reading_example.py',
    'pstail.py': 'tail_file_utility.py',
    'pstail2.py': 'tail_file_alternative.py',
    'pstailf.py': 'tail_file_follow.py',
    'greeting_program.py': 'simple_greeting_program.py',
    'beer_bottle_countdown.py': 'countdown_song_example.py',
    'odd_number_checker.py': 'odd_number_validator.py',
    'missing_numbers_sequence.py': 'sequence_missing_numbers.py',
    
    # Design Patterns
    'pssingleton02.py': 'singleton_pattern_v2.py',
    'pssingleton03.py': 'singleton_pattern_v3.py',
    'pssingletonsublime.py': 'singleton_pattern_alternative.py',
    
    # Testing & Examples
    'test_cases_1.py': 'unit_test_examples_1.py',
    'test_cases_2.py': 'unit_test_examples_2.py',
    'user_list_manager.py': 'list_management_utility.py',
    'quote_formatter.py': 'quote_formatting_basic.py',
    'quote_formatter_v2.py': 'quote_formatting_advanced.py',
    'data_structure_examples.py': 'data_structure_demo.py',
    'stdlib_examples.py': 'standard_library_examples.py',
    'operator_examples.py': 'operator_usage_examples.py',
    'variable_scope_demo.py': 'variable_scope_examples.py',
    'function_basics.py': 'function_fundamentals.py',
    'function_examples.py': 'function_usage_examples.py',
    'keyword_arguments_demo.py': 'keyword_arguments_example.py',
    
    # Network & System
    'ssh_client.py': 'ssh_client_utility.py',
}

def rename_files():
    """Rename files according to the mapping."""
    current_dir = Path('.')
    renamed_count = 0
    skipped_count = 0
    
    print("Starting file renaming process...")
    print("=" * 50)
    
    for old_name, new_name in file_rename_mapping.items():
        old_path = current_dir / old_name
        new_path = current_dir / new_name
        
        if old_path.exists():
            try:
                # Check if new name already exists
                if new_path.exists():
                    print(f"⚠️  Skipping '{old_name}' -> '{new_name}' (target already exists)")
                    skipped_count += 1
                    continue
                
                # Rename the file
                old_path.rename(new_path)
                print(f"✅ Renamed: '{old_name}' -> '{new_name}'")
                renamed_count += 1
                
            except Exception as e:
                print(f"❌ Error renaming '{old_name}': {e}")
                skipped_count += 1
        else:
            print(f"⚠️  File not found: '{old_name}'")
            skipped_count += 1
    
    print("=" * 50)
    print(f"Renaming complete!")
    print(f"✅ Successfully renamed: {renamed_count} files")
    print(f"⚠️  Skipped: {skipped_count} files")
    
    # Create a summary file
    with open('renaming_summary.txt', 'w') as f:
        f.write("File Renaming Summary\n")
        f.write("=" * 30 + "\n\n")
        f.write(f"Total files processed: {len(file_rename_mapping)}\n")
        f.write(f"Successfully renamed: {renamed_count}\n")
        f.write(f"Skipped: {skipped_count}\n\n")
        f.write("Renamed files:\n")
        f.write("-" * 20 + "\n")
        for old_name, new_name in file_rename_mapping.items():
            f.write(f"{old_name} -> {new_name}\n")
    
    print(f"\n📄 Summary saved to: renaming_summary.txt")

if __name__ == "__main__":
    # Change to the python_concepts directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print(f"Working directory: {os.getcwd()}")
    print(f"Script location: {script_dir}")
    
    # Confirm before proceeding
    response = input("\nDo you want to proceed with renaming the files? (y/N): ")
    if response.lower() in ['y', 'yes']:
        rename_files()
    else:
        print("File renaming cancelled.") 