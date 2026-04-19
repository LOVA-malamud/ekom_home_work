import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

# Game data
rate = [2, 3, 9, 7, 11]
symbol_names = ["CHERRY", "LEMON", "STAR", "BELL", "DIAMOND"]
symbol_colors = [RED, YELLOW, GOLD, SILVER, (185, 242, 255)]
money = 50

class SlotMachine:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Lucky Slot Machine")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        self.spin_result = [0, 0, 0]
        self.spinning = False
        self.spin_positions = [0, 0, 0]  # Current positions for spinning animation
        self.spin_speeds = [0, 0, 0]  # Speed for each reel
        self.spin_timers = [0, 0, 0]  # Timer for each reel to stop
        self.message = "Welcome! Place your bet!"
        self.bet_amount = 5
        self.money = money
        self.win_animation = 0
        
    def draw_symbol(self, symbol_idx, x, y, size=60):
        """Draw a symbol as a colored shape with text"""
        color = symbol_colors[symbol_idx]
        name = symbol_names[symbol_idx]
        
        # Draw background circle
        pygame.draw.circle(self.screen, color, (x, y), size)
        pygame.draw.circle(self.screen, BLACK, (x, y), size, 3)
        
        # Draw symbol text
        text = self.font_small.render(name[:3], True, BLACK)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)
        
        # Draw decorative elements based on symbol type
        if symbol_idx == 0:  # Cherry
            pygame.draw.circle(self.screen, RED, (x-15, y-10), 8)
            pygame.draw.circle(self.screen, RED, (x+15, y-10), 8)
        elif symbol_idx == 1:  # Lemon
            pygame.draw.ellipse(self.screen, YELLOW, (x-20, y-15, 40, 30), 3)
        elif symbol_idx == 2:  # Star
            self.draw_star(x, y, 25, GOLD)
        elif symbol_idx == 3:  # Bell
            pygame.draw.rect(self.screen, SILVER, (x-15, y-20, 30, 35), 3)
            pygame.draw.circle(self.screen, SILVER, (x, y-25), 8, 3)
        elif symbol_idx == 4:  # Diamond
            points = [(x, y-25), (x+20, y), (x, y+25), (x-20, y)]
            pygame.draw.polygon(self.screen, (185, 242, 255), points)
            pygame.draw.polygon(self.screen, BLACK, points, 3)
    
    def draw_reel(self, reel_idx, x, y):
        """Draw a single reel with spinning animation"""
        if self.spinning and self.spin_timers[reel_idx] > 0:
            # Spinning animation
            self.spin_positions[reel_idx] += self.spin_speeds[reel_idx]
            if self.spin_positions[reel_idx] >= len(symbol_names):
                self.spin_positions[reel_idx] = 0
            
            # Draw multiple symbols for spinning effect
            for i in range(-1, 2):
                symbol_idx = int(self.spin_positions[reel_idx] + i) % len(symbol_names)
                symbol_y = y + i * 80
                if 0 < symbol_y < WINDOW_HEIGHT:
                    self.draw_symbol(symbol_idx, x, symbol_y, 40)
            
            # Draw reel frame
            pygame.draw.rect(self.screen, DARK_GRAY, (x-70, y-60, 140, 120), 5)
            
        else:
            # Static symbol
            symbol_idx = self.spin_result[reel_idx]
            self.draw_symbol(symbol_idx, x, y, 60)
            
            # Draw reel frame
            pygame.draw.rect(self.screen, DARK_GRAY, (x-70, y-70, 140, 140), 5)
    
    def draw_slot_machine(self):
        """Draw the slot machine body"""
        # Main machine body
        machine_rect = pygame.Rect(100, 100, 500, 200)
        pygame.draw.rect(self.screen, DARK_GRAY, machine_rect)
        pygame.draw.rect(self.screen, BLACK, machine_rect, 5)
        
        # Reel windows
        for i in range(3):
            reel_x = 200 + i * 100
            reel_y = 200
            # Reel background
            pygame.draw.rect(self.screen, WHITE, (reel_x-70, reel_y-70, 140, 140))
            pygame.draw.rect(self.screen, BLACK, (reel_x-70, reel_y-70, 140, 140), 3)
        
        # Machine decoration
        pygame.draw.rect(self.screen, GOLD, (95, 95, 510, 10))  # Top trim
        pygame.draw.rect(self.screen, GOLD, (95, 295, 510, 10))  # Bottom trim
        
        # Title on machine
        title = self.font_small.render("LUCKY SLOTS", True, WHITE)
        title_rect = title.get_rect(center=(350, 120))
        self.screen.blit(title, title_rect)
    
    def draw_star(self, x, y, size, color):
        """Draw a star shape"""
        import math
        points = []
        for i in range(10):
            angle = math.pi * i / 5
            if i % 2 == 0:
                r = size
            else:
                r = size // 2
            px = x + r * math.cos(angle - math.pi/2)
            py = y + r * math.sin(angle - math.pi/2)
            points.append((px, py))
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, BLACK, points, 2)
    
    def start_spin(self):
        """Start the spinning animation"""
        if self.money >= self.bet_amount:
            self.spinning = True
            self.message = "Spinning..."
            
            # Generate final result
            self.spin_result = self.spin_slots()
            
            # Set up spinning animation
            for i in range(3):
                self.spin_positions[i] = random.random() * len(symbol_names)
                self.spin_speeds[i] = 0.5 + random.random() * 0.3
                # Reels stop at different times (1st stops first, 3rd stops last)
                self.spin_timers[i] = 60 + i * 30  # 1 second, 1.5 seconds, 2 seconds
            
            self.money -= self.bet_amount
        else:
            self.message = "Not enough money!"
    
    def spin_slots(self):
        """Generate random spin result"""
        return [random.randint(0, len(symbol_names) - 1) for _ in range(3)]
    
    def update_spinning(self):
        """Update spinning animation"""
        if self.spinning:
            all_stopped = True
            for i in range(3):
                if self.spin_timers[i] > 0:
                    self.spin_timers[i] -= 1
                    all_stopped = False
                else:
                    # Reel has stopped, ensure it shows the correct symbol
                    self.spin_positions[i] = self.spin_result[i]
            
            if all_stopped:
                self.spinning = False
                self.calculate_spin_result()
    
    def calculate_spin_result(self):
        """Calculate winnings after spin completes"""
        winnings = self.calculate_winnings(self.bet_amount, self.spin_result)
        
        if winnings > 0:
            self.money += winnings
            self.message = f"You won ${winnings}!"
            self.win_animation = 60  # 1 second of win animation
        else:
            self.message = f"You lost ${self.bet_amount}"
        
        if self.money <= 0:
            self.money = 0
            self.message = "GAME OVER! No money left!"
    
    def calculate_winnings(self, bet, spin_result):
        """Calculate winnings based on spin result"""
        symbol_counts = {}
        for idx in spin_result:
            symbol_counts[idx] = symbol_counts.get(idx, 0) + 1
        
        # Check for 3 of a kind
        for symbol_idx, count in symbol_counts.items():
            if count == 3:
                return bet * 777 * rate[symbol_idx]
        
        # Check for 2 of a kind
        for symbol_idx, count in symbol_counts.items():
            if count == 2:
                return bet * rate[symbol_idx]
        
        # All different - lose bet
        return 0
    
    def draw_button(self, text, x, y, width, height, color, hover_color):
        """Draw a button and return if clicked"""
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        
        button_rect = pygame.Rect(x, y, width, height)
        
        # Change color if hovering
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, hover_color, button_rect)
            if mouse_click:
                return True
        else:
            pygame.draw.rect(self.screen, color, button_rect)
        
        pygame.draw.rect(self.screen, BLACK, button_rect, 2)
        
        # Draw text
        text_surface = self.font_small.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)
        
        return False
    
    def draw(self):
        """Draw the entire game screen"""
        self.screen.fill(WHITE)
        
        # Draw title
        title = self.font_medium.render("=== LUCKY SLOTS ===", True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 30))
        self.screen.blit(title, title_rect)
        
        # Draw money
        money_color = GREEN if self.money > 0 else RED
        if self.win_animation > 0:
            money_color = GOLD
            self.win_animation -= 1
        money_text = self.font_medium.render(f"Money: ${self.money}", True, money_color)
        money_rect = money_text.get_rect(center=(WINDOW_WIDTH // 2, 70))
        self.screen.blit(money_text, money_rect)
        
        # Draw slot machine
        self.draw_slot_machine()
        
        # Draw reels
        for i in range(3):
            reel_x = 200 + i * 100
            reel_y = 200
            self.draw_reel(i, reel_x, reel_y)
        
        # Draw message
        msg_color = GOLD if self.win_animation > 0 else BLACK
        msg_surface = self.font_small.render(self.message, True, msg_color)
        msg_rect = msg_surface.get_rect(center=(WINDOW_WIDTH // 2, 330))
        self.screen.blit(msg_surface, msg_rect)
        
        # Draw bet amount
        bet_text = self.font_small.render(f"Bet: ${self.bet_amount}", True, BLACK)
        bet_rect = bet_text.get_rect(center=(100, 400))
        self.screen.blit(bet_text, bet_rect)
        
        # Draw buttons
        if not self.spinning:
            # Spin button
            if self.draw_button("SPIN", 250, 380, 100, 40, GREEN, (0, 200, 0)):
                self.start_spin()
            
            # Bet adjustment buttons
            if self.draw_button("-", 50, 380, 40, 40, GRAY, (100, 100, 100)):
                if self.bet_amount > 1:
                    self.bet_amount -= 1
            
            if self.draw_button("+", 150, 380, 40, 40, GRAY, (100, 100, 100)):
                if self.bet_amount < self.money:
                    self.bet_amount += 1
            
            # Quit button
            if self.draw_button("QUIT", 450, 380, 100, 40, RED, (200, 0, 0)):
                return False
        
        pygame.display.flip()
        return True
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            # Handle spinning animation
            self.update_spinning()
            
            # Draw everything
            if not self.draw():
                running = False
            
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# Run the game
if __name__ == "__main__":
    game = SlotMachine()
    game.run()
