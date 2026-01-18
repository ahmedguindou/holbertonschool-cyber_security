#!/usr/bin/env ruby
require 'json'

def count_user_ids(path)
  # Read and parse JSON file
  file_content = File.read(path)
  data = JSON.parse(file_content)
  
  # Count user IDs
  user_counts = Hash.new(0)
  
  data.each do |item|
    user_id = item['userId']
    user_counts[user_id] += 1 if user_id
  end
  
  # Sort and display results
  user_counts.sort.each do |user_id, count|
    puts "#{user_id}: #{count}"
  end
end
