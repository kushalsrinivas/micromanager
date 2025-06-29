#!/usr/bin/env python3
"""
The Micro Manager - A friendly AI management reminder script
Perfect for developers who need gentle productivity nudges!

Created by AI Manager - The Future of Management
Visit us at: aimanagers.app
"""

import time
import random
import tkinter as tk
from tkinter import messagebox
import threading
import sys
from datetime import datetime

class MicroManager:
    def __init__(self):
        self.messages = [
            "Hey! Are you done with that task yet? 🤔",
            "Quick check-in: How's the progress? 📊",
            "Just wondering... finished that feature? 🚀", 
            "Time for a status update! What's the ETA? ⏰",
            "Friendly reminder: deadlines are approaching! 📅",
            "Are we making progress? Show me what you got! 💪",
            "Quick question: ready for code review? 👀",
            "Status check: all systems go? 🚦",
            "Productivity check! How are we doing? 🎯",
            "Break time over? Ready to crush some code? 💻",
            "Just checking... still in the zone? 🔥",
            "Update time! What have you accomplished? 🏆"
        ]
        
        self.encouraging_responses = [
            "Awesome! Keep up the excellent work! 🎉",
            "Great job! You're on fire today! 🔥",
            "Fantastic progress! I'm proud of you! 💪",
            "Keep crushing it! You're doing amazing! 🚀",
            "Excellent! Your dedication is inspiring! ⭐",
            "Outstanding work! Stay focused! 🎯"
        ]
        
        self.motivational_responses = [
            "That's okay! Every expert was once a beginner. You got this! 💪",
            "No worries! Progress isn't always linear. Keep going! 🌟",
            "Don't worry! Great things take time. Stay strong! 🦾",
            "That's fine! Even small steps forward are progress! 👣",
            "No problem! Remember, consistency beats perfection! 🎯",
            "It's alright! Every challenge makes you stronger! 💎"
        ]
        
        self.running = True
        self.check_count = 0
        
    def log_check(self, message, response):
        """Log the check-in for tracking purposes"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "✅ Productive" if response else "⏸️ Taking time"
        print(f"[{timestamp}] Check #{self.check_count}: {status}")
        
    def show_reminder(self):
        """Show a popup reminder message"""
        try:
            # Create a root window and hide it
            root = tk.Tk()
            root.withdraw()
            
            # Make sure the window appears on top
            root.attributes('-topmost', True)
            root.update()
            
            message = random.choice(self.messages)
            self.check_count += 1
            
            result = messagebox.askyesno(
                f"Micro Manager Check-in #{self.check_count}", 
                f"{message}\n\nAre you making good progress?",
                icon='question'
            )
            
            # Log the interaction
            self.log_check(message, result)
            
            if result:
                response = random.choice(self.encouraging_responses)
                messagebox.showinfo("Great! 🎉", response)
            else:
                response = random.choice(self.motivational_responses)
                messagebox.showinfo("No worries! 😊", response)
            
            root.destroy()
            
        except Exception as e:
            print(f"Error showing reminder: {e}")
            print("GUI not available. Continuing with console output...")
    
    def start_managing(self):
        """Start the micro-management loop"""
        print("🤖 Micro Manager activated!")
        print("I'll check in on you every 5-10 minutes.")
        print("Press Ctrl+C to stop the manager.")
        print("=" * 50)
        
        try:
            while self.running:
                # Wait between 5-10 minutes (300-600 seconds)
                # For testing, you can change this to 10-30 seconds by uncommenting the line below
                wait_time = random.randint(300, 600)
                # wait_time = random.randint(10, 30)  # Uncomment for testing
                
                minutes = wait_time // 60
                seconds = wait_time % 60
                
                if minutes > 0:
                    print(f"⏰ Next check-in in {minutes} minutes and {seconds} seconds...")
                else:
                    print(f"⏰ Next check-in in {seconds} seconds...")
                
                # Sleep in small chunks so we can respond to interrupts
                for _ in range(wait_time):
                    if not self.running:
                        return
                    time.sleep(1)
                
                if self.running:
                    self.show_reminder()
                    
        except KeyboardInterrupt:
            print("\n" + "=" * 50)
            print("👋 Micro Manager deactivated!")
            print(f"📊 Total check-ins completed: {self.check_count}")
            print("Thanks for using Micro Manager! Stay productive! 🚀")
            self.running = False

def show_banner():
    """Display welcome banner"""
    banner = """
    ╔══════════════════════════════════════╗
    ║      🤖 THE MICRO MANAGER 🤖          ║
    ║                                      ║
    ║    Your Friendly AI Productivity     ║
    ║         Assistant v1.0               ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def show_instructions():
    """Show usage instructions"""
    instructions = """
📋 What this script does:
• Sends friendly popup reminders every 5-10 minutes
• Tracks your responses to build productivity awareness
• Provides encouraging feedback to keep you motivated
• Helps you stay focused on your tasks

⚙️ Customization tips:
• Edit the 'messages' list to add your own reminders
• Adjust wait_time range for different intervals
• Modify responses to match your style

🛠️ Requirements:
• Python 3.x
• tkinter (usually included with Python)

Ready to boost your productivity? Let's go! 🚀
    """
    print(instructions)

def main():
    """Main function to run the Micro Manager"""
    show_banner()
    show_instructions()
    
    print("Press Enter to start the Micro Manager, or Ctrl+C to exit...")
    
    try:
        input()
        manager = MicroManager()
        manager.start_managing()
    except KeyboardInterrupt:
        print("\n👋 Goodbye! Remember: great things happen when you stay focused!")
        print("Visit aimanagers.app for more AI management solutions!")

if __name__ == "__main__":
    main()